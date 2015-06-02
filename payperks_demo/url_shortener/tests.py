import json

from exam import Exam
from exam.mock import Mock
from exam import fixture
from exam.decorators import patcher

from django.conf import settings
from django.test.utils import override_settings
from django.core.urlresolvers import reverse
from django.test import TestCase

from payperks_demo.url_shortener.utils import short_string, LETTERS_AND_DIGITS
from payperks_demo.url_shortener.models import ShortenedURL


class TestShortString(TestCase):
    
    def test_short_string_returns_result_of_length(self):
        for i in range(10):
            result = short_string(length=i)
            self.assertEquals(len(result), i)

    def test_short_string_returns_unique_4_letters_and_digits(self):
        already_generated = []
        for i in range(100):
            result = short_string(already=already_generated)
            self.assertTrue(result not in already_generated)
            already_generated.append(result)
            for letter in result:
                self.assertTrue(letter in LETTERS_AND_DIGITS)
                

class TestShortenedURLViews(Exam, TestCase):
    
    @fixture
    def shortened_url(self):
        return ShortenedURL.objects.create(original='test/', shortened='uu')
    
    def test_api_root(self):
        resp = self.client.get(reverse('api:api-root'))
        self.assertEqual(resp.status_code, 200)
    
    def test_shortened_urls_list_view(self):
        resp = self.client.get(reverse('api:shortenedurl-list'))
        self.assertEqual(resp.status_code, 200)
        
    def test_shortened_urls_list_view_with_shortened_url(self):
        self.shortened_url
        resp = self.client.get(reverse('api:shortenedurl-list'))
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        self.assertEquals(data['results'], [{u'original': u'test/', u'shortened': u'uu'}])
        
    def test_shortened_urls_list_view_POST_shortened_url(self):
        resp = self.client.post(reverse('api:shortenedurl-list'), {'original': 'test_POST', 'shortened': ''})
        self.assertEqual(resp.status_code, 201)
        short_url = ShortenedURL.objects.get(original='test_POST')
        self.assertTrue(short_url.shortened)
    
    def test_unique_original_is_returned_on_second_request(self):
        resp = self.client.post(reverse('api:shortenedurl-list'), {'original': 'test_POST', 'shortened': ''})
        self.assertEqual(resp.status_code, 201)
        short_url = ShortenedURL.objects.get(original='test_POST')
        self.assertTrue(short_url.shortened)
        #second request
        resp = self.client.post(reverse('api:shortenedurl-list'), {'original': 'test_POST', 'shortened': ''})
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        self.assertEquals(data['original'], 'test_POST')
        
