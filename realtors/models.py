from django.db import models

# Create your models here.


class Realtor(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='')
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.name
