# _*_ coding:utf-8 _*_
__author__ = 'Bruse'
__date__ = '2017-02-14 22:14'

import xadmin
from .models import *


class OrderAdmin(object):
    pass


class OrderDetailAdmin(object):
    pass


xadmin.site.register(Order,OrderAdmin);
xadmin.site.register(OrderDetail,OrderDetailAdmin);