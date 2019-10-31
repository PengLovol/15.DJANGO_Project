from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# 作业：
# 		1.访问路径 http://localhost:8000/login
# 			交给 index 应用中的 login_views 去处理
# 		2.访问路径 http://localhost:8000/register
# 			交给 index 应用中的 register_views 去处理
# 		3.访问路径 http://localhost:8000/
# 			交给 index 应用中的 index_views 去处理
def login_views(request):
    return HttpResponse('<h1>这是login页面</h1>')


def register_views(request):
    return HttpResponse('<h1>这是register页面</h1>')

def index_views(request):
    return HttpResponse('<h1>这是网站的首页</h1>')