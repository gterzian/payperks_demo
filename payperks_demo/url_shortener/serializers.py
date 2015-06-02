from rest_framework import serializers

from payperks_demo.url_shortener.models import ShortenedURL


class  ShortenedUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ('original', 'shortened')