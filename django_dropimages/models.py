from django.db import models


class DropimagesGallery(models.Model):
    creation_timestamp = models.DateTimeField(auto_now_add=True)
