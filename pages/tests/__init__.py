from django.test import TestCase
from django.urls import reverse


class IndexTests(TestCase):
    def test_index_renders(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
