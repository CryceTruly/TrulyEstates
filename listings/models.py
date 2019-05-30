from django.db import models
from realtors.models import Realtor
# Create your models here.


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    list_date = models.DateTimeField(auto_now_add=True)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    is_published = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to="photos/%Y%m/%d/")
    photo1 = models.ImageField(upload_to="photos/%Y%m/%d/", blank=True)
    photo2 = models.ImageField(upload_to="photos/%Y%m/%d/", blank=True)
    photo3 = models.ImageField(upload_to="photos/%Y%m/%d/", blank=True)
    photo4 = models.ImageField(upload_to="photos/%Y%m/%d/", blank=True)
    photo5 = models.ImageField(upload_to="photos/%Y%m/%d/", blank=True)
    photo6 = models.ImageField(upload_to="photos/%Y%m/%d/", blank=True)

    def __str__(self):
        return self.title
