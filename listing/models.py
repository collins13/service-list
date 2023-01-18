from django.db import models

# Create your models here.


class Listing(models.Model):
    listing_name = models.CharField(max_length=255)
    listing_category = models.CharField(max_length=255)
    listing_image = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, null=True, max_length=255)
    listing_description = models.TextField(max_length=255)
    phone_no = models.CharField(max_length=255)
    listing_location = models.TextField(max_length=255)
    listing_address = models.TextField(max_length=255)


def __str__(self):
    return self.listing_name
