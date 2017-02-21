# _*_ coding:utf-8 _*_
__author__ = 'Bruse'
__date__ = '2017-02-16 14:42'

from django.conf.urls import url,include

from .views import *

urlpatterns = [
    url(r'^info/$',FightIndex.as_view(),name='index'),
    url(r'^detail/(?P<fight_id>.*)/$',FightDetail.as_view(),name='detail'),

]
