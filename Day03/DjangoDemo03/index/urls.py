from django.conf.urls import url
from .views import *

urlpatterns = [
  url(r'^01-parent/$',parent_views),
  url(r'^02-child/$',child_views),
  url(r'^03-test-alias/$',alias_views,name='alias'),
  url(r'^04-test-alias-params/(\d{4})/$',alias_params_views,name='params'),
  url(r'^05-reverse/$',reverse_views),
]