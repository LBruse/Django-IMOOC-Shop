# _*_ coding:utf-8 _*_
__author__ = 'Bruse'
__date__ = '2017-02-14 22:18'

from django.conf.urls import url,include


from account.views import *

urlpatterns = [
    url(r'^imc/$',LoginView.as_view(),name='imc_login'),

]