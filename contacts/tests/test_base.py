
from django.test import TestCase
from django.contrib.auth.models import User
from contacts.models import Contact


class BaseTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username="cryce", email="email@g.com",
            password="1234qwerq")
        self.contact = Contact.objects.create(listing='This is the Listing',
                                              email="emil@EMAIL.COM",
                                              message="hello need this",
                                              phone="076787373",
                                              user_id=1,
                                              realtor_email="realtor@email.com",
                                              listing_id=1,
                                              name="John Terry")
        self.data = {
            " listing_id": 1,
            " listing": 'listing',
            " name": 'name',
            "email": 'email',
            "phone": 'phone',
            "message": 'message',
            " user_id": 1,
            "realtor_email": 'realtor_email@gmail.com',

        }
        return super().setUp()
