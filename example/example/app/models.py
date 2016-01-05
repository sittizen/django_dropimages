from django.db import models


class SomeGallery(models.Model):
    title = models.CharField(max_length=128)
    dropimages_gallery = models.ForeignKey('django_dropimages.DropimagesGallery')
