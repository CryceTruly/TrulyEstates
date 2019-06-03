from django.test import TestCase
from listings.models import Listing
from realtors.models import Realtor


class RealtorModelTest(TestCase):
    def setUp(self):
        self.realtor = Realtor.objects.create(
            name="Cryce Truly", photo="", description="Hello")

        self.listing = Listing.objects.create(realtor=self.realtor,
                                              title="title",
                                              address="Address",
                                              city="City",
                                              zipcode="34554",
                                              description="description",
                                              price=1,
                                              bedrooms=1,
                                              bathrooms=1,
                                              garage=2,
                                              sqft=1,
                                              lot_size=2.3,
                                              photo_main="Image")

        return super().setUp()

    def test_should_create_a_listing(self):
        self.assertIsInstance(self.listing, Listing)
        self.assertEqual(str(self.listing), self.listing.title)
