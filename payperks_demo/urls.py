
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

from payperks_demo.url_shortener import views

router = routers.DefaultRouter()
router.register(r'short_urls', views.ShortenedUrlViewSet)

urlpatterns = [
    url(r'^/', views.home, name='home'),
    url(r'^(?P<short_url>[0-9a-zA-z]{4})/$', views.home_redirect, name='home_redirect'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls, namespace='api')),
]
