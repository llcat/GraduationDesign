/**
 * Created by ypl on 17-5-5.
 */

//前端通用组件模块，将大部分公用操作放在这个文件中

common= {

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
            for(var i=0;i<contents.length;i++){
                if(rawData[i].length>10){
                    contents.push(rawData[i].slice(0,10));
                }else{
                    contents.push(rawData[i]);
                }
            }
            var tag = "span";
            var re = common.generateTags(tag,contents);
            $("#word-panel").append(re);
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




