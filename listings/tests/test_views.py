from django.urls import reverse
from .test_models import ListingModelTest


class ListingsTest(ListingModelTest):

    def test_should_render_listings_page(self):
        response = self.client.get(reverse('listings'))
        self.assertEqual(response.status_code, 200)

    def test_should_render_search_page(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
