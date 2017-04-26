






try{
    flag = document.createElement('canvas');
}catch (e) {
    alert('your browser not support canvas,icon will lose');
}

//绘制 nav 的图标
var icon = document.getElementById('top-icon');
//获取绘制上下文
var ctx = icon.getContext('2d'),
    w = icon.width,
    h = icon.height;

var clusters = [];

function Point() {
    this.x = Math.round(Math.random()*w);
    this.y = Math.round(Math.random()*h);
}

//绘制
function draw_icon() {
    colors=['#9affb0','#FF23C0','#FFA895'];
    r1 = 20
    r = h/2 - r1*2
    ctx.translate(w/2,h/2);
    ctx.lineWidth = 1;
    angles=[90,210,330];
    delta = Math.PI/180;
    ctx.strokeStyle=colors[Math.round(Math.random()*3)];
    ctx.fillStyle=colors[Math.round(Math.random()*3)];
    setInterval(function () {
        ctx.clearRect(-w/2,-h/2,w,h);
        for(i=0;i<3;i++){
            angle = angles[i];
            //绘制3个圆
            x = r*Math.cos(angle*delta);
            y = r*Math.sin(angle*delta);
            drawARound(x,y,r1,ctx);
            //绘制链接圆心的三条线
        }
        if(angles[0]>360){
            ctx.strokeStyle=colors[Math.round(Math.random()*3)];
            ctx.fillStyle=colors[Math.round(Math.random()*3)];
        }
        for(i=0;i<3;i++){
            angles[i]+=5;
            if(i==0 && angles[i]>=450){
                angles[i] = 90;
            }
            if(i==1 && angles[i]>=(210+360)){
                angles[i] = 210;
            }
            if(i==3 && angles[i]>=(330+360)){
                angles[i] = 330;
            }
        }

    },Math.round(Math.random()*500));
}

function drawARound(x,y,r,ct) {
    ct.beginPath();
    ctx.arc(x,y,Math.random()*r/4,0,Math.PI*2)
    ctx.fill();
    ct.closePath();
    ct.beginPath();
    ct.arc(x,y,r,0,Math.PI*2);
    ctx.stroke()
    ctx.closePath();
}

draw_icon()