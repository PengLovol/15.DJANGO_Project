from django.conf.urls import url
from .views import *
urlpatterns = [
    #当访问路径是 http: // localhost: 8000 / news / index
    #则交给news的urls找到 index_views去处理
    url(r'^index/$',index_views),
    # 当访问路径是 http://localhost:8000/news/
    # 则交给news的urls找到 index_views去处理
    url(r'^$',index_views),
    ]