"""MyNetease URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  #当访问路径是 http://localhost:8000/music/xxxx
	#则交给music的urls去处理
  url(r'^music/',include('music.urls')),
  #当访问路径是 http://localhost:8000/news/xxxxx
	#则交给news的urls去处理
  url(r'^news/',include('news.urls')),

# 作业：
# 		1.访问路径 http://localhost:8000/login
# 			交给 index 应用中的 login_views 去处理
# 		2.访问路径 http://localhost:8000/register
# 			交给 index 应用中的 register_views 去处理
# 		3.访问路径 http://localhost:8000/
# 			交给 index 应用中的 index_views 去处理
  #只要访问路径不是 admin/**,music/**,news/** 的话，剩下的请求一律交给 index 应用去处理
  url(r'^',include('index.urls')),
]
