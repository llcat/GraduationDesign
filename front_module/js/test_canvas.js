/**
 * Created by ypl on 17-4-24.
 */
var cluster = document.getElementById('cluster');
var ctx = cluster.getContext('2d');
var w =ctx.canvas.width
var h = ctx.canvas.height

function draw() {
    ctx.fillStyle='#ff7567'
    ctx.lineWidth=1
    ctx.strokeStyle='#ff0000'
    r = w/4
    ctx.translate(w/2,h/2)
    ctx.beginPath()
    ctx.arc(w/4,0,r,0,2*Math.PI)
    ctx.stroke()
    ctx.closePath()
    ctx.beginPath()
    ctx.arc(0,-w/4,r,0,2*Math.PI)
    ctx.stroke()
    ctx.closePath()
    ctx.beginPath()
    ctx.arc(-w/4,0,r,0,2*Math.PI)
    ctx.stroke()
    ctx.closePath()
}

function draw_line() {
    setInterval(function () {
        ctx.strokeStyle = 'rgb(225,0,0)';
        ctx.fillStyle = 'rgb(0,255,0)';
        ctx.lineWidth=2;
        ctx.beginPath()
        ctx.translate(0,0)
        ctx.lineTo(0,0)
        ctx.lineTo(w/2,0)
        ctx.lineTo(0,h/2)
        ctx.stroke()
        ctx.rotate(20)
        ctx.closePath()
    },1000)

}

//绘制一个移动的圆
function drawMoveRound() {
    x = 0;
    y = 0;
    colors=['#d3bbff','#ff0000']
    ctx.lineWidth=0.5
    setInterval(function () {
        ctx.clearRect(0,0,w,h);
        ctx.beginPath();
        ctx.strokeStyle=colors[Math.round(Math.random()*2)];
        ctx.arc(x,y,Math.random()*10,0,Math.PI*2);
        ctx.stroke()
        vx = Math.random();
        vy = Math.random();
        x+= vx;
        y+= vy;
        if(x>w){
            x=0
        }
        if(y>h){
            y=0
        }
    },200)
}

//画三个联动的圆
function drawThreeRoundMove() {
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

    },100)
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
// draw()
// draw_line()
// drawMoveRound()
drawThreeRoundMove()