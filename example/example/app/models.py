from django.conf import settings
from django.db import models


class SomeGallery(models.Model):
    title = models.CharField(max_length=128)
    dropimages_gallery = models.ForeignKey('django_dropimages.DropimagesGallery')


if settings.DROP_IMAGES_CONFIG.get('DROPIMAGE_MODEL', None):
    class SomeImageModel(models.Model):
        my_image_field = models.ImageField(upload_to='/tmp/my_images/')

        dropimages_gallery = models.ForeignKey('django_dropimages.DropimagesGallery', related_name='images')
        dropimages_original_filename = models.CharField(max_length=256)
