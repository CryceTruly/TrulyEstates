from django.db import models
from listings.models import Listing
# Create your models here.


class Contact(models.Model):
    listing = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=35)
    name = models.CharField(max_length=35)
    user_id = models.IntegerField(blank=True)
    listing_id = models.IntegerField()
    realtor_email = models.EmailField()

    def __str__(self):
        return self.name
