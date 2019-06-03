from django.test import TestCase
from realtors.models import Realtor
from django.urls import reverse


class RealtorModelTest(TestCase):
    def setUp(self):
        self.realtor = Realtor.objects.create(name="Cryce Truly", photo="", description="Hello",
                                              email="crycetruly@gmail.com", phone="07567847444", is_mvp=False)

        return super().setUp()

    def test_should_create_a_realtor(self):
        self.assertIsInstance(self.realtor, Realtor)
        self.assertEqual(str(self.realtor), self.realtor.name)
