# _*_encoding:utf-8_*_

from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class SuperUser(AbstractUser):
    """
    管理后台--超级用户
    """
    nick_name=models.CharField(max_length=10,default='New',verbose_name=u"昵称");
    birthday=models.DateField(null=True,blank=True,verbose_name=u"生日");
    gender=models.CharField(choices=(("male",u"男"),("female",u"女")),default='male',max_length=5,verbose_name=u"性别");
    address=models.CharField(max_length=100,null=True,blank=True,verbose_name=u"住址");
    phone=models.CharField(max_length=11,null=True,blank=True,verbose_name=u"电话");
    image=models.ImageField(upload_to='image/superuser/%Y/%m',verbose_name=u"头像");

    class Meta:
        verbose_name=u"超级用户";
        verbose_name_plural=verbose_name;

    def __unicode__(self):
        return self.username;


class Account(models.Model):
    """
    用户
    """
    name=models.CharField(max_length=10,verbose_name=u"用户名");
    password=models.CharField(max_length=10,verbose_name=u"密码");
    email=models.EmailField(null=True,blank=True,verbose_name=u"邮箱");
    sex=models.CharField(choices=(("male",u"男"),("female",u"女")),default='male',max_length=5);
    phone=models.CharField(null=True,blank=True,max_length=11,verbose_name=u"手机");
    learn_time=models.IntegerField(default=0,verbose_name=u"学习时长");
    experience=models.IntegerField(default=0,verbose_name=u"经验");
    integral=models.IntegerField(default=0,verbose_name=u"积分");
    signature=models.CharField(max_length=20,default='Never give up',verbose_name=u"签名");
    image=models.ImageField(upload_to="image/user/%Y/%m",max_length=100,verbose_name=u"头像",default='');
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间");

    class Meta:
        verbose_name=u"用户";
        verbose_name_plural=verbose_name;

    def __unicode__(self):
        return self.name;


class QQ(models.Model):
    """
    第三方--QQ
    """
    nick_name=models.CharField(max_length=10,verbose_name=u"昵称");
    password=models.CharField(max_length=10,verbose_name=u"密码");
    email = models.EmailField(null=True, blank=True, verbose_name=u"邮箱");
    image=models.ImageField(upload_to="image/qq/%Y/%m",max_length=100,verbose_name=u"头像");
    account=models.ForeignKey(Account,verbose_name=u"用户",null=True,blank=True);

    class Meta:
        verbose_name=u"QQ";
        verbose_name_plural=verbose_name;

    def __unicode__(self):
        return self.qq_id;


class Sina(models.Model):
    """
    第三方--新浪
    """
    name=models.CharField(max_length=10,verbose_name=u"昵称");
    password=models.CharField(max_length=10,verbose_name=u"密码");
    email=models.EmailField(null=True,blank=True,verbose_name=u"邮箱");
    image=models.ImageField(upload_to="image/sina/%Y/%m",verbose_name=u"头像");
    account = models.ForeignKey(Account, verbose_name=u"用户", null=True, blank=True);

    class Meta:
        verbose_name=u"新浪";
        verbose_name_plural=verbose_name;

    def __unicode__(self):
        return self.name;


class WeChat(models.Model):
    """
    第三方--微信
    """
    name=models.CharField(max_length=10,verbose_name=u"昵称");
    password=models.CharField(max_length=10,verbose_name=u"密码");
    image=models.ImageField(upload_to="image/wechat/%Y/%m",verbose_name=u"头像");
    account = models.ForeignKey(Account, verbose_name=u"用户", null=True, blank=True);

    class Meta:
        verbose_name=u"微信";
        verbose_name_plural=verbose_name;

    def __unicode__(self):
        return self.name;



