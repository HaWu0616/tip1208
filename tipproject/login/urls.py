"""tipproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url

from django.contrib import admin
from tipproject import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.conf.urls import url, include
from login import views
# from monitor import views
from django.conf.urls import url
from django.contrib import admin

# 需要先导入对应app的views

urlpatterns = [
    # 参数第一部分为url的正则表达式，后面的是业务逻辑函数

    # admin后台路由
    url(r'^$', views.index),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),

]
urlpatterns += staticfiles_urlpatterns()
