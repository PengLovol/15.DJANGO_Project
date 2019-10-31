from django.conf.urls import url
from .views import *
urlpatterns=[
    url(r'^01_temp/',temp_views),
    url(r'^02_temp/',temp02_views),
    url(r'^03_var/',var_views),
    url(r'^04_static/$',static_views),
    url(r'^$',index_views),
]