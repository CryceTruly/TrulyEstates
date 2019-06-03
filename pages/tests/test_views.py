from django.test import TestCase
from django.urls import reverse


class PagesViewTest(TestCase):
    def test_should_render_homepage(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_should_render_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
