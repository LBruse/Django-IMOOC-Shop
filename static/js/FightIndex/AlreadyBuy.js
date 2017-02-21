/**
 * Created by acer1 on 2016-11-23.
 */
$(function(){
//         已购
    var already=$(".moco-modal");
    var alreadylink=$(".moco-modal-btns a");

//            获取页面高宽
    var height=$(document).height();
    var width=$(document).width();
    var clientHeight=$(window).height();

//            mask
    var mask=$("<div id='mask'></div>");
    mask.css({'width':width+'px','height':height+'px'});

//            添加隐藏层
    $("body").append(mask);
    already.css("display","block");

//            隐藏
    mask.add(alreadylink).click(function(event){
        event.preventDefault();
        mask.detach();
        already.css("display","none");
    });
});