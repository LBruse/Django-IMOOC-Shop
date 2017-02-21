# _*_ coding:utf-8 _*_
__author__ = 'Bruse'
__date__ = '2017-02-14 22:13'

import xadmin
from .models import *


class TypeAdmin(object):
    pass


class CourseAdmin(object):
    pass


xadmin.site.register(Type,TypeAdmin);
xadmin.site.register(Course,CourseAdmin);