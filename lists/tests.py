from django.http import HttpRequest, HttpResponse
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class HomePageTest(TestCase):
    """Тест домашней страницы"""
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    
    def test_home_page_returns_correct_html(self):
        """Test home page gives right response"""
        request = HttpRequest()
        response: HttpResponse = home_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
    