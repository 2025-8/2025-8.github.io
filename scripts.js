// 判断设备，若为手机跳转至移动端页面
var info = navigator.userAgent;
if (/mobile/i.test(info)) {
    // window.location.replace("./index_m.html");
    alert("这是给电脑看的页面，手机看着会很别扭");
}

//轮播图图片切换
var SUM_IMG=14;
var img_id=7;
function change_img(){
    var show_img=document.getElementById("show");
    var show_text=document.getElementById("show_text");
    var cd="https://cn.kstore.space/download/3696/2025-8/imgs/class/";
    // cd="./imgs/class/"
    show_img.src=cd+img_id.toString()+".jpg";
    show_text.innerHTML=texts[img_id];
}
function left_img(){
    if (img_id==1)img_id=SUM_IMG;
    else img_id-=1;
    change_img()
}
function right_img(){
    if (img_id==SUM_IMG)img_id=1;
    else img_id+=1;
    change_img()
}

//预加载展示图片
var url="https://cn.kstore.space/download/3696/2025-8/imgs/class/";
var images = new Array();
for (i = 1; i <= SUM_IMG; i++){  
    images[i] = new Image();
    images[i].src = url+i.toString()+".jpg";
}