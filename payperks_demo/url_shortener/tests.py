import json

from exam import Exam
from exam.mock import Mock
from exam import fixture
from exam.decorators import patcher

from django.conf import settings
from django.test.utils import override_settings
from django.core.urlresolvers import reverse
from django.test import TestCase

from payperks_demo.url_shortener.utils import short_string


class TestShortString(Exam, TestCase):
    
    def test_short_string_returns_letters_of_lenght(self):
        for i in range(10):
            result = short_string(length=i)
            self.assertEquals(len(result), i)

    def test_short_string_returns_unique_4_letters(self):
        already_generated = []
        for i in range(100):
            result = short_string(already=already_generated)
            self.assertTrue(result not in already_generated)
            already_generated.append(result)
        
