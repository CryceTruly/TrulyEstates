from django.test import TestCase
from listings.models import Listing
from realtors.models import Realtor
import mock
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from django.conf import settings

from io import StringIO
# in python 3: from io import StringIO
from PIL import Image
from django.core.files.base import File


class ListingModelTest(TestCase):
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
                                              photo_main="test")

        return super().setUp()

    def test_should_create_a_listing(self):
        self.assertIsInstance(self.listing, Listing)
        self.assertEqual(str(self.listing), self.listing.title)

    @staticmethod
    def get_image_file(name='test.png', ext='png', size=(50, 50), color=(256, 0, 0)):
        file_obj = StringIO()
        image = Image.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)
