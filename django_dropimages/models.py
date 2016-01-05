from django.conf import settings
from django.db import models


class DropimagesGallery(models.Model):
    gallery_identifier = models.CharField(max_length=36)
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)


class DropimagesImage(models.Model):
    gallery = models.ForeignKey('django_dropimages.DropimagesGallery', related_name='images')
    image = models.ImageField(upload_to='%y/%m/%d')
    original_filename = models.CharField(max_length=256)
