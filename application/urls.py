from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from application import views
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

#router = DefaultRouter()
#router.register(r'application', views.ApplicationViewSet, base_name = 'application')
#router.register(r'user', views.UserViewSet)
#schema_view = get_schema_view(title = 'Pastebin API')

urlpatterns = [
   #url(r'^', include(router.urls)),
   #url(r'^schema/$', schema_view),
   url(r'^application/$', views.ApplicationViewSet.as_view(), name = 'application'),
   url(r'^users/$', views.UserViewSet, name = 'users'),
   url(r'^questions/$', views.questions, name = 'questions'),
]