from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from django_dropimages import settings as di_settings


class DropImagesConfig(AppConfig):
    name = 'django_dropimages'
    verbose_name = _("Django DropImages")

    def ready(self):
        di_settings.patch_all()
