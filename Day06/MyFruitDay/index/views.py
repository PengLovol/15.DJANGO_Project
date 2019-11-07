from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def login_views(request):
    return render(request,'login.html')

def register_views(request):
    # 判断是get请求还是post请求，得到用户的请求意图
    if request.method=='GET':
        return render(request,'register.html')
    else:
        # 先验证手机号在数据库中是否存在
        uphone=request.POST['uphone']
        users=User.objects.filter(uphone=uphone)
        if users:
            # uphone 已经存在
            errMsg='手机号码已经存在'
            return render(request,'register.html',locals())
        # 接收数据插入到数据库中
        upwd=request.POST['upwd']
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        user=User()
        user.uphone=uphone
        user.upwd=upwd
        user.uname=uname
        user.uemail=uemail
        user.save()
        return HttpResponse('注册成功')