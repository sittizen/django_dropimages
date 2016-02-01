from __future__ import absolute_import, unicode_literals
from importlib import import_module

from django.conf import settings

# Always import this module as follows:
# from django_dropimages import settings [as di_settings]

CONFIG_DEFAULTS = {
    'DICT_DEFAULT_MESSAGE': 'To upload drop here files, a directory or click.',

    'SHOW_ID_ON_COMPLETE': None,
    'GALLERY_FIELD_ID': None,
    'UPLOAD_URL': None,
    'DELETE_URL': None,

    'DROPIMAGE_MODEL': None,
    'DROPIMAGE_FIELD': None,
}

USER_CONFIG = getattr(settings, 'DROP_IMAGES_CONFIG', {})

CONFIG = CONFIG_DEFAULTS.copy()
CONFIG.update(USER_CONFIG)


# The following functions can monkey-patch settings automatically. Several
# imports are placed inside functions to make it safe to import this module.


def patch_root_urlconf():
    from django.conf.urls import include, url
    from django.core.urlresolvers import clear_url_caches, reverse, NoReverseMatch
    import django_dropimages
    try:
        reverse('djdropimages:upload')
    except NoReverseMatch:
        urlconf_module = import_module(settings.ROOT_URLCONF)
        urlconf_module.urlpatterns = [
            url(r'^__dropimages__/', include(django_dropimages.urls)),
        ] + urlconf_module.urlpatterns
        clear_url_caches()


def patch_all():
    pass
    #patch_root_urlconf()  # copied from django debug toolbar but seems to not work in some cases #todo
