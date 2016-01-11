from django.conf import settings
from django.db import models

from django_dropimages import settings as di_settings


class DropimagesGallery(models.Model):
    gallery_identifier = models.CharField(max_length=36)
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

# if no custom image models is present I load my own
if not di_settings.CONFIG['DROPIMAGE_MODEL']:
    class DropimagesImage(models.Model):
        dropimages_gallery = models.ForeignKey('django_dropimages.DropimagesGallery', related_name='images')
        dropimages_original_filename = models.CharField(max_length=256)
        image = models.ImageField(upload_to='%y/%m/%d')
