/**
 * Created by acer1 on 2016-11-29.
 */
<!--显示导航-->

$(function(){
//            侧栏nav
    var nav=$(".menuContent .item");

//            nav详细
    var nav_detail=$(".submenu");

    nav.mouseover(function(){
    show_nav("in",$(this).index());

    });

    nav_detail.mouseover(function(){
        $(this).show();
    });

    nav.mouseout(function(){
    show_nav("out",$(this).index());
    });

    nav_detail.mouseout(function(){
        $(this).hide();
    });

//            显示nav
    function show_nav(action,index){
//            nav 下标
    var nav_index=0;
    nav_index=index;
    if(action=="in"){
    nav_detail.eq(nav_index).show();
    }else{
    nav_detail.eq(nav_index).hide();
    };
    };
    });
