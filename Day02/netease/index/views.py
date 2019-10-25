from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login_views(request):
  return HttpResponse("<h1>这是login页面</h1>")

def register_views(request):
  return HttpResponse("<h1>这是register页面</h1>")

def index_views(request):
  return HttpResponse("<h1>这是网站的首页</h1>")