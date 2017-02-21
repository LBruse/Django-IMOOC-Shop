# _*_encoding:utf-8_*_

import json
import random

from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.base import View
from django.core.urlresolvers import reverse

from .models import *
from .forms import *
from course.models import Course
from order.models import *

# Create your views here.


class IndexView(View):
    """
    主页
    """
    def get(self,request):

        # 验证码
        captcha_form=CaptchaForm();

        # 用户
        account=None;
        if (len(request.session._session)>0):
            account_id = request.session['account_id'];
            account = Account.objects.get(id=account_id);


        # 实战

        # 用户订单
        order=Order.objects.filter(account=account);

        fight_list=list(Course.objects.all());

        # 主页中的实战推荐不显示用户已购买的课程
        for detail in order:
            if detail.is_pay == 1:
                for course in detail.orderdetail_set.all():
                    fight_list.remove(Course.objects.get(id=course.course_id));

        random_fight=random.sample(fight_list,5);

        return render(request,'Index.html',{
            'captcha_form':captcha_form,
            'account':account,
            'fight_list':random_fight
        });

    # 注册
    def post(self,request):
        register_form=CaptchaForm(request.POST);
        if register_form.is_valid():
            register=request.POST.get('register','');
            register_pwd=request.POST.get('registerPwd','');

            if Account.objects.filter(Q(email=register)|Q(phone=register)):
                return HttpResponse('{"status":"fail","msg":"已占用"}',content_type='application/json');

            account=Account();
            account_name='第'+str(Account.objects.all().count()+1)+'位慕粉';
            if '@' in register:
                account.email=register;
            elif len(register):
                account.phone=register;
            account.password=register_pwd;
            account.name=account_name;
            account.save();

            return HttpResponse('{"status":"success","msg":"已注册"}', content_type='application/json');

        return HttpResponse('{"status":"fail","msg":"输入错误"}', content_type='application/json');


class LoginView(View):
    """
    登录
    """
    def post(self,request):
        login_form=LoginForm(request.POST);
        if login_form.is_valid():
            user_name=request.POST.get('login');
            user_pwd=request.POST.get('pwd');
            user=Account.objects.get(Q(email=user_name)|Q(phone=user_name),password=user_pwd);
            # user=authenticate(username=user_name,password=user_pwd);
            if user is not None:
                request.session['account_id']=user.id;
                # return render(request,'Index.html',{
                #     'account':user
                # });
                return HttpResponseRedirect(reverse('index'));
                # return HttpResponse('{"status":"fail","msg":"用户不存在"}',content_type='application/json');
        else:
            return render(request,'Index.html',{});
            # return HttpResponse('{"status":"fail","msg":"输入有误"}',content_type='application/json');


class AccountInfo(View):
    """
    个人页面
    """
    def get(self,request):
        account_id=request.session['account_id'];
        account=Account.objects.get(id=account_id);
        return render(request,'account/RecentNews.html',{
            'account':account
        });


class LogoutView(View):
    """
    退出
    """
    def get(self,request):
        del request.session['account_id'];
        return HttpResponseRedirect(reverse('index'));


