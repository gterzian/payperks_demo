from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from payperks_demo.url_shortener.models import ShortenedURL
from payperks_demo.url_shortener.serializers import ShortenedUrlSerializer


def home(request):
    context = {}
    context['short_urls'] = ShortenedURL.objects.all()
    return render(request, 'url_shortener/index.html', context)


def short_url_redirect(request, short_url):
    url = get_object_or_404(ShortenedURL, shortened=short_url)
    return HttpResponseRedirect(url.original)
    

def create_new_shortened_url(request):
    '''In case of an existing shortened url for the original, we return the existing one'''
    if ShortenedURL.objects.filter(original=request.POST['original']).exists():
        shortened_url = ShortenedURL.objects.get(original=request.POST['original'])
        serializer = ShortenedUrlSerializer(shortened_url)
    else:
        serializer = ShortenedUrlSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
    return HttpResponseRedirect('/#url_list')


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
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = ShortenedUrlSerializer(data=request.POST)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)
               
