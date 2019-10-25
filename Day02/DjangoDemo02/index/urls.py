from django.conf.urls import url
from .views import *

urlpatterns = [
  url(r'^01-temp/$',temp_views),
  url(r'^02-temp/$',temp02_views),
  url(r'^03-var/$',var_views),
  url(r'^04-static/$',static_views),
  url(r'^$',index_views),
]