function courseHover(){
//            获取所有课程list
    var wrap=$(".course-wrap");

//            简介动态效果
    $(".course-wrap").mouseover(function(){
        $(this).find(".course-info").css("top","30px");
        $(this).css("box-shadow","0 5px 20px 2px rgba(0,0,0,0.3)");
    }).mouseout(function(){
        $(this).find(".course-info").css("top","65px");
        $(this).css("box-shadow","0 5px 10px 0 rgba(0,0,0,0.1)");
    });

}
