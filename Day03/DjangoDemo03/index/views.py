from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def parent_views(request):
  return render(request,'01-parent.html')

def child_views(request):
  return render(request,'02-child.html')

def alias_views(request):
  return HttpResponse("成功访问到03-test-alias路径")

def alias_params_views(request,year):
  return HttpResponse('<h1>传递进来的参数为:%s</h1>' % year)

def reverse_views(request):
  # 将alias别名解析成对应的地址并输出
  url1 = reverse('alias')
  print('alias的地址为:%s' % url1)
  # 将params别名以及参数解析成对应的地址并输出
  url2 = reverse('params',args=('2018',))
  print('params的地址为:%s' % url2)
  return HttpResponse("解析成功")