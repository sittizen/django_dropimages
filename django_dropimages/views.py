from django.shortcuts import get_object_or_404
from django.views.generic import View
from braces.views import CsrfExemptMixin, JSONResponseMixin

from django_dropimages import settings as di_settings
from .models import DropimagesGallery

from django.apps import apps


class UploadView(CsrfExemptMixin, JSONResponseMixin, View):
    def post(self, request, *args, **kwargs):
        owner = request.user if not request.user.is_anonymous() else None
        image = request.FILES['file']
        gallery, _ = DropimagesGallery.objects.get_or_create(gallery_identifier=request.GET['gallery_id'],
                                                             owner=owner)
        image_klass = apps.get_model(di_settings.CONFIG['DROPIMAGE_MODEL'] or 'django_dropimages.DropimagesImage')
        kwargs_dict = {
            'dropimages_gallery': gallery,
            'dropimages_original_filename': image._name,
            di_settings.CONFIG['DROPIMAGE_FIELD'] or 'image': image
        }
        image_klass.objects.create(**kwargs_dict)
        return self.render_json_response({
            'gallery_identifier': request.GET['gallery_id'],
            'gallery_pk': gallery.pk,
            'file_name': image._name,
        })


class DeleteView(CsrfExemptMixin, JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        owner = request.user if not request.user.is_anonymous() else None
        gallery = get_object_or_404(DropimagesGallery, gallery_identifier=request.GET['gallery_id'], owner=owner)
        image_klass = apps.get_model(di_settings.CONFIG['DROPIMAGE_MODEL'] or 'django_dropimages.DropimagesImage')
        di = get_object_or_404(image_klass, dropimages_gallery=gallery,
                               dropimages_original_filename=request.GET['original_filename'])
        di.delete()
        return self.render_json_response({})
