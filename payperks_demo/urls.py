
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

from payperks_demo.url_shortener import views

router = routers.DefaultRouter()
router.register(r'short_urls', views.ShortenedUrlViewSet)

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^create/$', views.create_new_shortened_url, name='create_new_shortened_url'),
    url(r'^m/(?P<short_url>[0-9a-zA-z]{4})/$', views.short_url_redirect, name='short_url_redirect'),
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^(?P<full_url>.+)$', views.redirected, name='redirected'),
    
]
