from django.conf.urls import url
from .views import *
urlpatterns=[
    #http://localhost:8000/01_parent
    url(r'^01-parent/$', parent_views,name='parent'),
    #http://localhost:8000/01_child
    url(r'^02-child/$', child_views,name='child'),
    #http://localhost:8000/03-arguments/四位整数/两位整数
    url(r'^03-arguments/(\d{4})/(\d{2})',arguments_views,name='arg'),
    ##http://localhost:8000/04-reverse
    url(r'04-reverse/',reverse_views),

]

urlpatterns+=[
#http://localhost:8000/05-add
    url(r'^05-add/$', add_views, name='add'),
]