from rest_framework import viewsets

from payperks_demo.url_shortener.models import ShortenedURL
from payperks_demo.url_shortener.serializers import ShortenedUrlSerializer



class ShortenedUrlViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shortened urls to be viewed or edited.
    """
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedUrlSerializer
