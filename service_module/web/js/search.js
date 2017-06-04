/**
 * Created by ypl on 17-5-1.
 */
search_page_operate={
    //search页面初始化相关操作
    init:function () {
        $('#search-btn').click(function () {
            common.events.search.cb_search_btn_click();
            $(".history-word").each(function (index) {
                $(this).click(function () {
                    common.events.home.cb_history_word_click(index);
                })
            });
        });

//初始化页面时显示历史记录
        common.history.show();

//历史搜索词绑定点击事件
        $(".history-word").each(function (index) {
            $(this).click(function () {
                common.events.home.cb_history_word_click(index);
            })
        });

        $("#delete-button").click(function () {
            common.history.removeAll();
            common.history.show();
        });
    },

    showResults:function () {
        var key = $("#keyword").text();
        var page = 1;
        var baseUrl = "http://localhost:8080/";
        var tags = ['div','a','div',];
        var csses =['result-panel','result-title','divide',];
        var tags1 = ['div','span'];
        var csses1 = ['result-related-infos','related-info']
        var resultPanel = common.genarateDom(tags, csses);
        var relatedInfos = common.genarateDom(tags1,csses1);
        // console.log(resultPanel);
        // console.log(relatedInfos);
        //请求关键字查询结果
        $.get(baseUrl+"search/"+key).done(function (data) {
            search_page_operate.dataBindByKey("#key-result",resultPanel,data);
        });
        $.get(baseUrl+"searchInTags/"+key+"/"+page).done(function (data) {
            search_page_operate.dataBindByTag("#tag-result",resultPanel,data,1);
        });

        //请求聚类结果，实际上返回了相关样本点的邻域
        $.get(baseUrl+"searchByCluster/"+key+"/"+page).done(function (data) {
            search_page_operate.dataBindByCluster("#cluster-result",resultPanel,data);
        })
    },
    //给相关组件添加行为绑定
    actionBind:function () {
        //给翻页组件绑定点击事件
        //完成的功能简单，清空先前生成的节点信息
        //重新发送请求，并重新绑定一遍数据
        function showChange(page) {
            $("#tag-result").empty();
            var key = $("#keyword").text();
            var baseUrl = "http://localhost:8080/";
            var tags = ['div','a','div',];
            var csses =['result-panel','result-title','divide',];
            var resultPanel = common.genarateDom(tags, csses);
            $.get(baseUrl+"searchInTags/"+key+"/"+page).done(function (data) {
                search_page_operate.dataBindByTag("#tag-result",resultPanel,data,page);
            });
        }

        $("#tag-up").click(function () {
            if(pageTag<1){
                pageTag = 1;
            }else{
                pageTag -= 1;
            }
            showChange(pageTag);
        });
        $("#tag-down").click(function () {
            if(pageTag<1){
                pageTag = 1;
            }else{
                pageTag += 1;
            }
            console.log("in tag-down click, page is:",pageTag);
            showChange(pageTag);
        });
    },
    dataBindByKey:function (root, resultPanel, data) {
        var tags1 = ['div','span']
        var csses1 = ['result-related-infos','related-info']
        if(data.length == 0){
            $('#choice-key').attr("data-forbidden",0);
        }else{
            $('#choice-key').attr("data-forbidden",1);
        }
        for(var i=0;i<data.length;i++) {
            var panel = $(resultPanel);
            var relatedInfo = search_page_operate.generateRelatedInfo(tags1,csses1,data[i]);
            panel.attr("data-title",data[i]['lemma_title']);
            panel.children(".result-title").text(data[i]['lemma_title']);
            panel.append(relatedInfo);
            $(root).append(panel);
            console.log(panel)
        }
    },
    //数据绑定到相关的dom上
    dataBindByTag:function (root,resultPanel,data,curPage) {
        var d = data.data;
        var l = d.length;
        var tags1 = ['div','span']
        var csses1 = ['result-related-infos','related-info']
        if(l == 0){
            $('#choice-tag').attr("data-forbidden",0);
        }else{
            //alert(d.length);
            $('#choice-tag').attr("data-forbidden",1);
        }
        if (l != 0) {
            for(var i=0;i<l;i++) {
                var panel = $(resultPanel);
                var relatedInfo = search_page_operate.generateRelatedInfoOtherData(tags1,csses1,d[i])
                panel.children(".result-title").text(d[i]['lemmaTitle']);
                panel.append(relatedInfo);
                //根据当前页面数生成排名
                var rank = (curPage-1)*10+i+1;
                var rankInfo = "<div class='rank-info'>"+rank+"</div>";
                panel.append(rankInfo);
                $(root).append(panel);
                console.log(panel)
            }
        }
        //判断data.total的值，看是否需要添加分页组件
        if(data.total > 10){
            var pageList = search_page_operate.generatePageList(data.total,curPage,1);
            $(root).append(pageList);
            search_page_operate.actionBind();
        }
    },
    dataBindByCluster:function (root,resultPanel,data) {
        var tags1 = ['div','span'];
        var csses1 = ['result-related-infos','related-info'];
        var d = data.data;
        var l = d.length;
        if(l == 0){
            $('#choice-cluster').attr("data-forbidden",0);
        }else{
            $('#choice-cluster').attr("data-forbidden",1);
        }
        if (l != 0) {
            for(var i=0;i<l;i++) {
                var panel = $(resultPanel);
                var relatedInfo = search_page_operate.generateRelatedInfoOtherData(tags1,csses1,d[i])
                panel.children(".result-title").text(d[i]['lemmaTitle']);
                panel.append(relatedInfo);
                $(root).append(panel);
                console.log(panel)
            }
        }
    },

    generateRelatedInfo:function (tags,csses,data) {
        var p = "<" + tags[0]+" class="+csses[0]+">";
        var view = "<"+tags[1]+" class="+csses[1]+">"+"<i class=\"fa fa-eye\"></i>"+data['history_view_count']+"</span>";
        var like = "<"+tags[1]+" class="+csses[1]+">"+"<i class=\"fa fa-heart\"></i>"+data['like_count']+"</span>";
        var share = "<"+tags[1]+" class="+csses[1]+">"+"<i class=\"fa fa-share-alt\"></i>"+data['share_count']+"</span>";
        var edit = "<"+tags[1]+" class="+csses[1]+">"+"<i class=\"fa fa-edit\"></i>"+data['history_edit_count']+"</span>";
        return p+view+like+share+edit+"</"+tags[0]+">";
    },

    //两种数据返回的格式有点不一样，理论上应该做一次数据格式化的,但是我太懒了。。。。
    generateRelatedInfoOtherData:function (tags,csses,data) {
        var p = "<" + tags[0]+" class="+csses[0]+">";
        var view = "<"+tags[1]+" class="+csses[1]+">"+"<i class=\"fa fa-eye\"></i>"+data['historyViewCount']+"</span>";
        var like = "<"+tags[1]+" class="+csses[1]+">"+"<i class=\"fa fa-heart\"></i>"+data['likeCount']+"</span>";
        var share = "<"+tags[1]+" class="+csses[1]+">"+"<i class=\"fa fa-share-alt\"></i>"+data['shareCount']+"</span>";
        var edit = "<"+tags[1]+" class="+csses[1]+">"+"<i class=\"fa fa-edit\"></i>"+data['editCount']+"</span>";
        return p+view+like+share+edit+"</"+tags[0]+">";
    },
    //如果查询结果集大于10条，进行分页，提供生成分页组件的函数
    //仅仅给标签结果和簇标记结果提供分页
    generatePageList:function (total, page, label) {
        //label为1,html中change的id是tag-up,tag-down
        //label为2,html中change的id是cluster-up,cluster-down
        var pageNum = Math.ceil(total/10);
        var initInfo = page+"页/"+pageNum+"页";
        var html ="";
        if(label==1){
            html = "<div class='page-list'>"+
                "<div id='tag-up' class='change'>上一页</div><div id='tag-down' class='change'>下一页</div>"+"<div class='page-info'>"+initInfo+"</div>"+"</div>"

        }else if(label==2){
            html = "<div class='page-list'>"+
                "<div id='cluster-up' class='change'>上一页</div><div id='cluster-down' class='change'>下一页</div>"+"<div class='page-info'>"+initInfo+"</div>"+"</div>"
        }
        return html;
    }
};

var pageTag = 1;
search_page_operate.init();
search_page_operate.showResults();