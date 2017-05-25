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
        var tags1 = ['div','span']
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
            search_page_operate.dataBindByTag("#tag-result",resultPanel,data);
        });

        //请求聚类结果，实际上返回了相关样本点的邻域
        $.get(baseUrl+"searchByCluster/"+key+"/"+page).done(function (data) {
            search_page_operate.dataBindByCluster("#cluster-result",resultPanel,data);
        })
    },
    //给相关组件添加行为绑定
    actionBind:function () {

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
    dataBindByTag:function (root,resultPanel,data) {
        var d = data.data;
        var l = d.length;
        var tags1 = ['div','span']
        var csses1 = ['result-related-infos','related-info']
        if(l == 0){
            $('#choice-tag').attr("data-forbidden",0);
        }else{
            alert(d.length);
            $('#choice-tag').attr("data-forbidden",1);
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
    dataBindByCluster:function (root,resultPanel,data) {
        var tags1 = ['div','span']
        var csses1 = ['result-related-infos','related-info']
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
    generateRelatedInfoOtherData:function (tags,csses,data) {
        var p = "<" + tags[0]+" class="+csses[0]+">";
        var view = "<"+tags[1]+" class="+csses[1]+">"+"<i class=\"fa fa-eye\"></i>"+data['historyViewCount']+"</span>";
        var like = "<"+tags[1]+" class="+csses[1]+">"+"<i class=\"fa fa-heart\"></i>"+data['likeCount']+"</span>";
        var share = "<"+tags[1]+" class="+csses[1]+">"+"<i class=\"fa fa-share-alt\"></i>"+data['shareCount']+"</span>";
        var edit = "<"+tags[1]+" class="+csses[1]+">"+"<i class=\"fa fa-edit\"></i>"+data['editCount']+"</span>";
        return p+view+like+share+edit+"</"+tags[0]+">";
    }

};

search_page_operate.init();
search_page_operate.showResults();
