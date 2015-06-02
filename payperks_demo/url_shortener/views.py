from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from payperks_demo.url_shortener.models import ShortenedURL
from payperks_demo.url_shortener.serializers import ShortenedUrlSerializer



class ShortenedUrlViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shortened urls to be viewed or edited.
    """
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedUrlSerializer
    
    def create(self, request):
        '''In case of an existing shortened url for the original, we return the existing one'''
        if ShortenedURL.objects.filter(original=request.POST['original']).exists():
            shortened_url = ShortenedURL.objects.get(original=request.POST['original'])
            serializer = ShortenedUrlSerializer(shortened_url)
        else:
            serializer = ShortenedUrlSerializer(data=request.POST)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_200_OK)
