# _*_encoding:utf-8_*_

"""PIMOOC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve
from PIMOOC.settings import MEDIA_ROOT

import xadmin

from account.views import *
from course.views import *

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^login/',include('account.urls',namespace='login')),
    url(r'^register/$',IndexView.as_view(),name='register'),
    url(r'^logout/',LogoutView.as_view(),name='logout'),
    url(r'^account_info/$',AccountInfo.as_view(),name='account_info'),
    url(r'^shop/',include('order.urls',namespace='shop')),
    url(r'^fight/',include('course.urls',namespace='fight')),

    # 验证码
    url(r'^captcha/',include('captcha.urls')),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]
