from django.conf.urls import url
from .views import *
# 作业：
# 		1.访问路径 http://localhost:8000/login
# 			交给 index 应用中的 login_views 去处理
# 		2.访问路径 http://localhost:8000/register
# 			交给 index 应用中的 register_views 去处理
# 		3.访问路径 http://localhost:8000/
# 			交给 index 应用中的 index_views 去处理
urlpatterns=[
    # 如果请求路径是login的话，则交给login_views去处理
    url(r'^login/$',login_views),
    #如果请求路径是register的话，则交给register_views去处理
    url(r'^register/$',register_views),
    #如果请求路径是　/ 的话，则交给index_views去处理
    url(r'^$',index_views),
]
