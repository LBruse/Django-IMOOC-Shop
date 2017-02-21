# _*_encoding:utf-8_*_

import json
import time

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse

from .models import *
from course.models import *
from account.models import Account

# Create your views here.


class CartView(View):
    """
    购物车
    """
    def get(self,request,fight_id):

        # 用户
        if (len(request.session._session) > 0):
            account_id = request.session['account_id'];
            account = Account.objects.get(id=account_id);

        # 添加到购物车
        if(int(fight_id)>0):
            fight=Course.objects.get(id=int(fight_id));

            if not(Cart.objects.filter(account=account, course=fight)):
                cart=Cart();
                cart.account=account;
                cart.course=fight;
                cart.save();

        # 购物车中的课程
        cart_fights=Cart.objects.filter(account=account);
        fights=[fight.course for fight in cart_fights ];
        fight_num=len(fights);

        return render(request,'shop/Cart.html',{
            'fights':fights,
            'fight_num':fight_num
        });


class DelCartView(View):
    """
    从购物车中删除
    """
    def get(self,request,fight_id):
        if(len(request.session._session)>0):
            account=Account.objects.get(id=int(request.session['account_id']));

        fight=Course.objects.get(id=int(fight_id));
        cart=Cart.objects.get(account=account,course=fight);
        cart.delete();

        return HttpResponseRedirect(reverse('shop:cart',kwargs={'fight_id':0}));


class SettlementView(View):
    """
    结算
    """
    def post(self,request):
        # 用户
        if (len(request.session._session) > 0):
            account = Account.objects.get(id=int(request.session['account_id']));

        # 唯一订单号
        local_time=time.localtime(time.time());
        order_id=str(local_time.tm_year)+str(local_time.tm_mon)+str(local_time.tm_mday)+str(local_time.tm_hour)+str(local_time.tm_min)+str(local_time.tm_sec)+str(local_time.tm_sec);

        # 总价
        total_price=0;

        # 选中的课程
        check_item=request.POST.getlist('checkItem');
        fights=[];
        for id in check_item:
            del_cart=Cart.objects.filter(course_id=id);
            if del_cart:
                del_cart.delete();

            fight=Course.objects.get(id=id);
            fights.append(fight);
            total_price+=fight.price;


        # 订单生成
        order=Order();
        order.order_id=order_id;
        order.price=total_price;
        order.account=account;
        order.save();

        # 订单详情
        for fight in fights:
            order_detail=OrderDetail();
            order_detail.course=fight;
            order_detail.order=order;
            order_detail.save();

            # 从购物车中删除
            cart = Cart.objects.filter(account=account, course=fight);
            if cart:
                cart.delete();

        return HttpResponseRedirect(reverse('shop:pay',kwargs={'order_id':order.order_id,'pay_way':0}));


class PayView(View):
    """
    支付页面
    """
    def get(self,request,order_id,pay_way):
        order=Order.objects.get(order_id=order_id);
        order_detail=OrderDetail.objects.filter(order=order);
        fights=[];
        for detail in order_detail:
            fights.append(detail.course);

        return render(request,'pay/Pay.html',{
            'order':order,
            'fights':fights
        });

    def post(self,request,order_id,pay_way):

        # 完成订单
        order=Order.objects.get(order_id=order_id);
        order.is_pay=True;
        if int(pay_way)==1:
            order.pay_way='zfb';
        elif int(pay_way)==2:
            order.pay_way='wx';
        order.save();

        return HttpResponse('{"status":"success",}', content_type='application/json');


class PayHistory(View):
    """
    历史订单
    """
    def get(self,request):
        # 用户
        if (len(request.session._session) > 0):
            account = Account.objects.get(id=int(request.session['account_id']));

        # 所有订单
        orders = Order.objects.filter(account=account).order_by('-add_date');
        fights = OrderDetail.objects.all();
        courses = Course.objects.all();

        # 订单数量
        order_nums = orders.count();

        # 购物车数量
        cart_nums=Cart.objects.filter(account=account).count();

        return render(request, 'pay/PayHistory.html', {
            'orders': orders,
            'fights': fights,
            'order_nums': order_nums,
            'courses': courses,
            'cart_nums':cart_nums
        });


class CancelPayView(View):
    """
    取消订单
    """
    def get(self,request,order_id):
        order=Order.objects.get(order_id=order_id);
        order.is_pay=2;
        order.save();

        return HttpResponseRedirect(reverse('shop:pay_history'));
