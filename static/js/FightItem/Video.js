$(function(){
    //          静态视频
    var videoInfo=$(".videoInfo");

//           播放按钮
    var play=videoInfo.find("i");
//            容器
    var playWrap=document.getElementById("videoPlay");
//          动态视频
    var video=document.getElementById("video");
//            关闭视频
    var stop=$("#videoPlay i");

    play.click(function(){
//                隐藏静态
        videoInfo.hide();
//                显示动态
        playWrap.style.display="block";
        video.style.width="100%";
        video.style.height="100%";
        video.play();
    });

    stop.click(function(){
//                静态显示
        videoInfo.show();

        video.pause();
        playWrap.style.display="none";
    });

});
