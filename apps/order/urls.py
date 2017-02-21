# _*_ coding:utf-8 _*_
__author__ = 'Bruse'
__date__ = '2017-02-16 22:13'

from django.conf.urls import url,include

from .views import *

urlpatterns = [
    url(r'^cart/(?P<fight_id>\d+)/$',CartView.as_view(),name='cart'),
    url(r'^del_cart/(?P<fight_id>\d+)/$',DelCartView.as_view(),name='del_cart'),
    url(r'^settlement/$',SettlementView.as_view(),name='settlement'),
    url(r'^pay/(?P<order_id>.*)/(?P<pay_way>\d+)/$',PayView.as_view(),name='pay'),
    url(r'^pay_history/$',PayHistory.as_view(),name='pay_history'),
    url(r'^cancel_pay/(?P<order_id>.*)/$',CancelPayView.as_view(),name='cancel_pay'),
]