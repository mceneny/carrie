from django.test import TestCase, Client
from django.urls import reverse
from .views import IndexView


class TestUrls(TestCase):

    def test_index(self):
        index = reverse('home:index')
        self.assertEquals(index, '/')


class TestViews(TestCase):

    def test_indexview(self):
        client = Client()
        response = client.get(reverse('home:index'))
        self.assertEqual(response.status_code, 200)