/**
 * Created by acer1 on 2016-11-17.
 */
<!--jQuery-->

$(function(){
    var loginLink=$(".logined a[name=loginLink]");
    var registerLink=$(".logined a[name=registerLink]");
//            登录窗体
    var signin=$("#signin");
//            关闭
    var close=$(".sign-header button");
//            登录title
    var signTitle=$(".sign-header h1 span:first-child");
//            注册title
    var registerTitle=$(".sign-header h1 span:last-child");
//            登录表单
    var signForm=$("#signForm");
//            注册表单
    var registerForm=$("#registerForm");

//            获取页面高宽
    var height=$(document).height();
    var width=$(document).width();
    var clientHeight=$(window).height();

//            mask
    var mask=$("<div id='mask'></div>");
    mask.css({'width':width+'px','height':height+'px'});

//          弹出层
    loginLink.click(function(e){
        e.preventDefault;
        $("body").append(mask);
        signin.css("display","block");
        Switch(signTitle,registerTitle,signForm,registerForm);
    })

    registerLink.click(function(e){
        e.preventDefault;
        $("body").append(mask);
        signin.css("display","block");
        Switch(registerTitle,signTitle,registerForm,signForm);
    })

    close.click(function(){
    mask.detach();
    signin.css("display","none");
    });

    mask.click(function(){
    mask.detach();
    signin.css("display","none");
    });


//            登录，注册切换
    signTitle.click(function(){
    Switch(signTitle,registerTitle,signForm,registerForm);
    });
    registerTitle.click(function(){
    Switch(registerTitle,signTitle,registerForm,signForm);
    });

//            注册密码显示
    var register=$("input[name=register]");
    var registerPwd=$("input[name=registerPwd]");
    register.keyup(function(){
    if(register.val()!=""){
    registerPwd.css("display","block");
    }else{
    registerPwd.val("");
    registerPwd.css("display","none");
    }
    });

    });

//            登录，注册切换
function Switch(add,remove,block,none){
    add.addClass('active');
    remove.removeClass('active');
    block.css("display","block");
    none.css("display","none");
    }
