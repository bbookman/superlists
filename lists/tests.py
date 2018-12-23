from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.http import HttpResponse
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):


    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTemplateUsed(response, 'home.html')
