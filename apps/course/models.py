# _*_encoding:utf-8_*_

from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class Type(models.Model):
    """
    课程类型
    """
    name=models.CharField(max_length=10,verbose_name=u"名称");
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间");

    class Meta:
        verbose_name=u"课程类型";
        verbose_name_plural=verbose_name;

    def __unicode__(self):
        return self.name;


class Course(models.Model):
    """
    课程
    """
    name=models.CharField(max_length=20,verbose_name=u"名称");
    type=models.ForeignKey(Type,verbose_name=u"类型");
    students=models.IntegerField(default=0,verbose_name=u"学习人数");
    click_nums=models.IntegerField(default=0,verbose_name=u"点击数");
    degree=models.CharField(choices=(('low',u"初级"),('middle',u"中级"),('high',u"高级")),default='high',max_length=10,verbose_name=u"难度");
    length=models.IntegerField(default=0,verbose_name=u"时长");
    score=models.IntegerField(default=0,verbose_name=u"评分");
    abstract=models.CharField(max_length=50,verbose_name=u"简述");
    detail=models.CharField(max_length=100,verbose_name=u"详细描述");
    image=models.ImageField(upload_to='image/course/%Y/%m',max_length=50,verbose_name=u"图片");
    is_fight=models.CharField(choices=(('y',u"是"),('n',u'否')),default='n',max_length=1,verbose_name=u"是否实战");
    price=models.IntegerField(default=0,verbose_name=u"价格");
    cloud_service=models.IntegerField(default=0,verbose_name=u"云服务天数");
    add_date=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间");

    class Meta:
        verbose_name=u"课程";
        verbose_name_plural=verbose_name;

    def __unicode__(self):
        return self.name;


