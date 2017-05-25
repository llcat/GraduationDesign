/**
 * Created by ypl on 17-5-5.
 */

//前端通用组件模块，将大部分公用操作放在这个文件中

common= {
    baseUrl:"http://localhost:8080/",
    history:{
        //存储历史查询记录
        storage:function(searchWord){
            if(typeof(Storage) != 'undefined'){
                var myStorage = localStorage;
                if(myStorage.getItem("words") == undefined){
                    var words = {
                        data:[searchWord]
                    };
                    //alert(JSON.stringify(words));
                    myStorage.setItem("words",JSON.stringify(words));
                }else{
                    var s_words = myStorage.getItem("words");
                    var hisWords = JSON.parse(s_words);
                    if(hisWords['data'].indexOf(searchWord)!=-1){
                        //alert("历史中存在");
                    }else {
                        if(hisWords.data.length>=10){
                            hisWords.data.shift();
                            hisWords.data.push(searchWord);
                        }else{
                            hisWords.data.push(searchWord);
                        }
                    }
                    myStorage.setItem("words",JSON.stringify(hisWords));
                }
            }else{
                alert("your browser not support H5 Storage")
            }
        },

        //以json形式返回所有的历史查询记录
        getAll:function () {
            var s_words = localStorage.getItem("words");
            var result = JSON.parse(s_words);
            return result;
        },

        //清除所有的历史记录
        removeAll:function () {
            var words = common.history.getAll();
            words.data = [];
            localStorage.setItem("words",JSON.stringify(words));
        },

        show:function () {
            var rawData = common.history.getAll().data;
            var contents = [];
            for(var i=0;i<rawData.length;i++){
                if(rawData[i].length>13){
                    contents.push(rawData[i].slice(0,10)+"...");
                }else{
                    contents.push(rawData[i]);
                }
            }
            var tag = "span";
            var re = common.generateTags(tag,contents);
            $("#word-panel").empty();
            $("#word-panel").append(re);
            $("#word-panel span").addClass("history-word");
            var spans = $(".history-word");
            spans.each(function (index) {
                $(this).attr("data-history-word",rawData[index]);
            })
        }

    },
    /**
     * 给定标签名
     * @param tag
     * @param contents
     */
    generateTags:function (tag,contents) {
        var re = "";
        for(var i=0;i<contents.length;i++){
            re += "<"+tag+">"+contents[i]+"</"+tag+">";
        }
        return re;
    },
    //根据传入的标签名和id或者class数组生成一颗两层的dom树，如果css数组长度一，子节点不添加id或class,如果长度为2,为所有子节点添加相同class,如果长度大于3,那么节点数目与css数组长度相等
    //如果tags数组长度为3,且tags[2]为数字，并保证css数组长度为2,生成一组指定数目的相同节点
    genarateDom:function (tags, csses) {
        if(tags.length==0){
            return "tags length is 0";
        }
        if(tags.length!=0 && csses.length==0){
            var p = "<"+tags[0]+">";
            for(var i=1;i<tags.length;i++){
                p += "<"+tags[i]+"></"+tags[i]+">";
            }
            p+="</"+tags[0]+">";
            return p;
        }
        //对多个不同的tag赋予不同的class
        if(tags.length == csses.length){
            var p = "<"+tags[0]+" class=\""+csses[0]+"\""+">";
            for(var i=1;i<tags.length;i++){
                p+="<"+tags[i]+" class=\""+csses[i]+"\""+">"+"</"+tags[i]+">";
            }
            p += "</"+tags[0]+">";
            return p;
        }
        //对多个相同的tag赋予相同的class
        if(tags.length==3&&csses.length==2){
            var p = "<"+tags[0]+" id=\""+csses[0]+"\""+">";
            for(var i=0;i<tags[2];i++){
                p += "<"+tags[1]+" class=\""+csses[1]+"\""+">"+"</"+tags[1]+">";
            }
            p += "</"+tags[0]+">";
            return p;
        }
        return "error";
    },
    //封装所有的通用组件的事件响应回调函数
    events:{
        home:{
            cb_search_btn_click:function () {
                //alert("in cb_search_btn");
                var q = $("#search-input").val();
                var path ="result-list/"+q;
                common.history.storage(q);
                common.history.show();
                window.open(path,"_blank");
            },
            cb_history_word_click:function (index) {
                //alert($(".history-word").eq(index).attr("data-history-word"));
                var word= $(".history-word").eq(index).attr("data-history-word");
                $("#search-input").val(word);
            }
        },

        search:{
            cb_search_btn_click:function () {
                var q = $("#search-input").val();
                var path =common.baseUrl+"result-list/"+q;
                common.history.storage(q);
                common.history.show();
                window.open(path,"_blank");
            },

        },

        detail:{

        }
    },
    site_icon: {
        id:"top-icon",
        colors:['#9affb0','#FF23C0','#FFA895'],
        icon: function () {
            return document.getElementById(this.id);
        },
        ctx: function () {
            return this.icon().getContext("2d");
        },
        draw_round: function (x, y, r, ct) {
            ct.beginPath();
            ct.arc(x, y, Math.random() * r / 4, 0, Math.PI * 2)
            ct.fill();
            ct.closePath();
            ct.beginPath();
            ct.arc(x, y, r, 0, Math.PI * 2);
            ct.stroke()
            ct.closePath();
        },
        draw: function (r) {
            //确定运动轨迹圆的半径
            //alert('start draw');
            var w = this.icon().width;
            var h = this.icon().height;
            var orbit_r = h/2 - 2*r;
            var ctx = this.ctx();
            //alert(w+"\n"+h+"\n"+orbit_r+"\n"+r);
            ctx.translate(w/2,h/2);
            ctx.lineWidth = 1;
            var start_angles=[90,210,330];
            var delta = Math.PI/180;
            ctx.strokeStyle=common.site_icon.colors[Math.round(Math.random()*3)];
            ctx.fillStyle=common.site_icon.colors[Math.round(Math.random()*3)];
            setInterval(function () {
                ctx.clearRect(-w/2,-h/2,w,h);
                for(var i=0;i<3;i++){
                    angle = start_angles[i];
                    //绘制3个圆
                    x = orbit_r*Math.cos(angle*delta);
                    y = orbit_r*Math.sin(angle*delta);
                    common.site_icon.draw_round(x,y,r,ctx);
                }
                if(start_angles[0]>360){
                    ctx.strokeStyle=common.site_icon.colors[Math.round(Math.random()*3)];
                    ctx.fillStyle=common.site_icon.colors[Math.round(Math.random()*3)];
                }
                for(i=0;i<3;i++){
                    start_angles[i]+=5;
                    if(i==0 && start_angles[i]>=450){
                        start_angles[i] = 90;
                    }
                    if(i==1 && start_angles[i]>=(210+360)){
                        start_angles[i] = 210;
                    }
                    if(i==3 && start_angles[i]>=(330+360)){
                        start_angles[i] = 330;
                    }
                }

            },Math.round(Math.random()*500));
        }
    },

};

common.site_icon.draw(20);





