from django.test import TestCase
from .test_base import BaseTest


class ContactModelTest(BaseTest):
    def test_should_create_a_contact(self):
        self.assertEqual(str(self.contact), self.contact.name)
