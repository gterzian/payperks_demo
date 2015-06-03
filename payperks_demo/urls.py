
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

from payperks_demo.url_shortener import views

router = routers.DefaultRouter()
router.register(r'short_urls', views.ShortenedUrlViewSet)

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^m/(?P<short_url>[0-9a-zA-z]{4})/$', views.short_url_redirect, name='short_url_redirect'),
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^.+$', views.home, name='home'),
    
]
