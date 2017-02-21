# _*_encoding:utf-8_*_

from __future__ import unicode_literals

from datetime import datetime

from django.db import models

from account.models import Account
from course.models import Course

# Create your models here.


class Order(models.Model):
    """
    订单
    """
    order_id=models.BigIntegerField(primary_key=True,verbose_name=u"订单号");
    account=models.ForeignKey(Account,verbose_name=u"用户");
    price=models.IntegerField(default=0,verbose_name=u"总金额");
    is_pay=models.IntegerField(choices=((0,u"未支付"),(1,u"已支付"),(2,u"关闭")),default=0,verbose_name=u"是否支付");
    pay_way=models.CharField(choices=(('wx',u"微信"),('zfb',u"支付宝")),default='zfb',max_length=3,verbose_name=u"支付方式");
    add_date=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间");

    class Meta:
        verbose_name=u"订单";
        verbose_name_plural=verbose_name;

    def __unicode__(self):
        return self.order_id;


class OrderDetail(models.Model):
    """
    订单详细
    """
    order=models.ForeignKey(Order,verbose_name=u"订单");
    course=models.ForeignKey(Course,verbose_name=u"课程");
    add_date=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间");

    class Meta:
        verbose_name=u"订单详情";
        verbose_name_plural=verbose_name;

    def __unicode__(self):
        return self.order.order_id;


class Cart(models.Model):
    """
    购物车
    """
    account=models.ForeignKey(Account,verbose_name=u"用户");
    course=models.ForeignKey(Course,verbose_name=u"实战");
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间");

