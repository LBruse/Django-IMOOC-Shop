# _*_ coding:utf-8 _*_
__author__ = 'Bruse'
__date__ = '2017-02-14 18:30'

from django import forms
from captcha.fields import CaptchaField

from .models import Account


class CaptchaForm(forms.Form):
    """
    验证码
    """

    register=forms.CharField(required=True);
    registerPwd=forms.CharField(required=True,min_length=6,max_length=10);
    captcha=CaptchaField(error_messages={'invalid':u"验证码错误"});


class RegisterForm(forms.ModelForm):
    """
    注册
    """
    class Meta:
        model=Account;
        fields=['password'];


class LoginForm(forms.Form):
    """
    登录
    """
    login=forms.CharField(required=True);
    pwd=forms.CharField(required=True,min_length=6,max_length=10);