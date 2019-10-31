from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
from django.urls import reverse


def parent_views(request):
    list=['首页','服装鞋帽','食品','夺宝']
    return render(request,'01-parent.html',locals())

def child_views(request):
    list = ['首页', '服装鞋帽', '食品', '夺宝']
    return render(request,'02-child.html',locals())

def arguments_views(request,year,month):
    return HttpResponse('年份为：'+year+'月份为:'+month)

def reverse_views(request):
    # url=reverse('parent')
    url = reverse('arg',args=('2018','12') )
    return HttpResponse('解析的地址为：'+url)

#http://localhost:8000/05-add
def add_views(request):
    # 方案１：Entry.objects.create()
    obj = Author.objects.create(name='王老师', age=32, email='wang.wc@163.com')
    print(obj.id, obj.name, obj.age, obj.email)
    return HttpResponse('Add OK')