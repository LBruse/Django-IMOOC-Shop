# _*_encoding:utf-8_*_

import random

from django.shortcuts import render
from django.views.generic.base import View

from .models import *
from order.models import *

# Create your views here.


class FightIndex(View):
    """
    实战主页
    """
    def get(self,request):
        all_fight=random.sample(Course.objects.all(),len(Course.objects.all()));

        # 用户
        if (len(request.session._session) > 0):
            account = Account.objects.get(id=int(request.session['account_id']));

        order=Order.objects.filter(account=account);
        account_fights=[];
        for detail in order:
            if detail.is_pay==1:
                for course in detail.orderdetail_set.all():
                    account_fights.append(Course.objects.get(id=course.course_id));

        return render(request,'fight/FightIndex.html',{
            'all_fight':all_fight,
            'account_fights':account_fights
        });


class FightDetail(View):
    """
    实战详情
    """
    def get(self,request,fight_id):
        id=int(fight_id);
        fight=Course.objects.get(id=fight_id);
        return render(request,'fight/FightBase.html',{
            'fight':fight
        });

