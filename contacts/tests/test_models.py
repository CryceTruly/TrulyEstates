from django.test import TestCase
from contacts.models import Contact


class ContactModelTest(TestCase):
    def test_should_create_a_contact(self):
        self.contact = Contact.objects.create(listing='This is the Listing', email="emil@EMAIL.COM", message="hello need this", phone="076787373",
                                              user_id=1, realtor_email="realtor@email.com", listing_id=1, name="John Terry")
        self.assertEqual(str(self.contact), self.contact.name)
