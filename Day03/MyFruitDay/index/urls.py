from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns =[
    url(r'^login$',login_views),
    url(r'^register$',register_views),
]