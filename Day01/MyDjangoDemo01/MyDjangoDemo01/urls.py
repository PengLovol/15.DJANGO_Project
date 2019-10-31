"""MyDjangoDemo01 URL Configuration

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
from  .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^show/$',show_views ),
    # url(r'^sh',sh_views),
    #访问路径是show/两位i数字，交给show1_views去处理
    url(r'^show/(\d{2})/$',show1_views),
    #访问路径是/四位数字/两位数字/两位数字  交给show2_views
    url(r'^show/(\d{4})/(\d{2})/(\d{2})/$',show2_views),
    #访问路径是/show3的时候，交给show3_views去处理
    url(r'^show3/$',show3_views,{'name':'naruto','age':18}),
]