# coding:utf-8
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from login.forms import  LoginForm,RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django import forms
from django.db import models
from login.models import User
import hashlib

import os
import time
import sys
import atexit
import psutil
import platform


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.method == "POST":
        email = request.POST.get('log_email', None)
        password = request.POST.get('log_password', None)    # 确保当数据请求中没有对应键时不会抛出异常
        message = "所有字段都必须填写！"
        if email and password:  # 确保用户名和密码都不为空
            email = email.strip()  # 邮箱地址符合法性验证
            try:
                user = User.objects.get(email=email)
                if user.password == hash_code(password):
                    return redirect('/login/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'login/login.html', {"message": message})
    return render(request, 'login/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['reg_username']
        email = request.POST['reg_email']
        password1 = request.POST['reg_password1']
        password2 = request.POST['reg_password2']
        phone = request.POST['reg_phone']
        message ="所有字段必须填写完整！"
        if password1!=password2:
            message ="两次输入的密码不一致！"
        else:
            if User.objects.filter(username=username):
                message = "该用户已注册！"
            else:
                if User.objects.filter(email=email):
                    message = "该邮箱已注册！"
                else:
                    new_user = User.objects.create()
                    new_user.username = username
                    new_user.password = hash_code(password1)  # 加盐哈希密码加密
                    new_user.email = email
                    new_user.phone = phone
                    new_user.save()
                    return redirect('/login/index')
    return render(request, 'login/login.html', locals())


def hash_code(s, salt='login'): # 对密码哈希加盐加密
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


 #    def get_memory(self):
 #        '''获取内存总数'''
 #        return int(psutil.virtual_memory().total/(1027*1024))
 #    def get_memory_percent(self):
 #        '''获取内存使用率'''
 #        return (str)(psutil.virtual_memory().percent)
 #    def start_time(self):
 #        '''获取开机时间'''
 #        return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(psutil.boot_time()))
 #    def drive_used(self):
 #        '''获取磁盘使用状况'''
 #        result = []
 #        for i in psutil.disk_partitions():
 #            result.append((i[0],psutil.disk_usage(i[1])[3]))
 #        return result
 #    def Net_io(self):
 #        '''获取网络速率'''
 #        if self.flag == 0:
 #            r1 = psutil.net_io_counters().bytes_recv
 #        else:
 #            r1 = self.flag
 #        r2 = psutil.net_io_counters().bytes_recv
 #        self.flag = r2
 #        y = r2 - r1
 #        return (y / 1024.0)
 #    def get_uname(self):
 #        '''获取系统信息，不需要刷新，分别为
 #        (操作系统类型,计算机名称,版本,版本号,位数,处理器信息,处理器名称)'''
 #        return platform.uname(),(self.start_time())
 #    def get_hardware_info(self):
 #        '''需要动态刷新的硬件信息，需要刷新，包括：
 #        (CPU使用率,内存总数,内存使用率,磁盘使用总数及使用率,网络使用率)'''
 #        return (self.get_cpu_percent(),self.get_memory(),self.get_memory_percent(),self.drive_used(),self.Net_io())
 #
 # if __name__ == '__main__':
 #        test = get_Systeminfo()
 #        print(test.get_hardware_info())
 #        # while True:
 #        #     print test.Net_io()
 #        #     print test.get_uname()
 #        #     print test.get_hardware_info()
 #        #     time.sleep(1)
 #
 #
 #
 #    #def logout(request):
 #    #auth.logout(request)
 #    #return render(request, 'login/index.html', locals())
