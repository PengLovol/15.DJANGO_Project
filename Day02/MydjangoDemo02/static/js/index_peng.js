/**
 * Created by Lenovo on 2019/10/5.
 */
window.onload=function () {
//    1.获取元素节点
    var currentAddr=document.getElementsByClassName('currentAddress')[0];
    var select=document.getElementsByClassName('select')[0];

        // 获取内层列表中的地址项
    var address=select.children;

    //为每一项添加点击事件
    for (var i=0;i<address.length;i++){
        address[i].onclick=function () {
          //传值
            currentAddr.innerHTML=this.innerHTML;
        };
    }
//    ------图片轮播---------------
    //1.获取图片数组
    //2.定时器实现图片切换
    //3.图片切换主要切换数组下标 ，防止数组越界
    var banner=document.getElementsByClassName('wrapper')[0];
    var imgs=banner.children; //图片数组

    var imgNav=document.getElementsByClassName('imgNav')[0];
    var indInfo=imgNav.children;//索引数组

    var imgIndex=0;//初始下标
    var timer;
    timer=setInterval(autoPlay,2000);//定时器
    function autoPlay() {
        //设置元素隐藏与显示
        imgs[imgIndex].style.display="none";
        // ++ imgIndex;
        // if(imgIndex==imgs.length){
        //     imgIndex=0;
        // }

        imgIndex=++ imgIndex==imgs.length ? 0: imgIndex;
        imgs[imgIndex].style.display="block";

        //切换索引 切换背景色
        for(var i=0;i<indInfo.length;i++){

         indInfo[i].style.background="gray";
        }
        indInfo[imgIndex].style.background='red';

    }
    //鼠标移入
    banner.onmousemove=function () {
        //停止定时器
        clearInterval(timer);
    };
    //鼠标移出
    banner.onmouseout=function () {
        timer=setInterval(autoPlay,1000);
    };

};