from django.conf.urls import url
from .views import *

#主要实现music应用中的地址与视图的处理
# 访问路径是　http://localhost:8000/music/xxx 的时候回交给当前的urls处理
# 该文件中，只需要处理　music/ 后面的路径即可
urlpatterns = [
  # 当访问路径是　index 的时候，交给index_views去处理
  url(r'^index/$',index_views),
]
