from rest_framework import serializers

from payperks_demo.url_shortener.models import ShortenedURL
from payperks_demo.url_shortener.utils import short_string


class  ShortenedUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ('original', 'shortened')
        
    def create(self, validated_data):
        validated_data['shortened'] = short_string(already=[url[0] for url in ShortenedURL.objects.values_list('shortened')])
        return ShortenedURL.objects.create(**validated_data)