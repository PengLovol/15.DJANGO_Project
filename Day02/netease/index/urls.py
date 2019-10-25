from django.conf.urls import url
from .views import *

urlpatterns = [
  #如果请求路径是login的话，则交给login_views去处理
  url(r'^login/$',login_views),
  #如果请求路径是register的话，则交给register_views去处理
  url(r'^register/$',register_views),
  #如果请求路径是　/ 的话，则交给index_views去处理
  url(r'^$',index_views),
]