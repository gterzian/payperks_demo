
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

from payperks_demo.url_shortener import views

router = routers.DefaultRouter()
router.register(r'short_urls', views.ShortenedUrlViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls, namespace='api')),
]
