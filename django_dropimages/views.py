from django.apps import apps
from django.shortcuts import get_object_or_404
from django.views.generic import View
from braces.views import CsrfExemptMixin, JSONResponseMixin

from django_dropimages import settings as di_settings


class UploadView(CsrfExemptMixin, JSONResponseMixin, View):
    def post(self, request, *args, **kwargs):
        try:
            owner = request.user if not request.user.is_anonymous() else None
            image = request.FILES['file']

            gallery_klass = apps.get_model(di_settings.CONFIG['DROPIMAGEGALLERY_MODEL'] or 'django_dropimages.DropimagesGallery')
            kwargs_dict = {
                'gallery_identifier': request.GET['gallery_id'],
                di_settings.CONFIG['DROPIMAGEOWNER_FIELD'] or 'owner': owner
            }
            gallery, _ = gallery_klass.objects.get_or_create(**kwargs_dict)

            image_klass = apps.get_model(di_settings.CONFIG['DROPIMAGE_MODEL'] or 'django_dropimages.DropimagesImage')
            kwargs_dict = {
                'dropimages_gallery': gallery,
                'dropimages_original_filename': image._name,
                di_settings.CONFIG['DROPIMAGE_FIELD'] or 'image': image,
                di_settings.CONFIG['DROPIMAGEOWNER_FIELD'] or 'owner': owner
            }
            image_klass.objects.create(**kwargs_dict)

            return self.render_json_response({
                'gallery_identifier': request.GET['gallery_id'],
                'gallery_pk': gallery.pk,
                'file_name': image._name,
            })
        except Exception, e:
            print str(e)


class DeleteView(CsrfExemptMixin, JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        owner = request.user if not request.user.is_anonymous() else None

        gallery_klass = apps.get_model(di_settings.CONFIG['DROPIMAGEGALLERY_MODEL'] or 'django_dropimages.DropimagesGallery')
        gallery = get_object_or_404(gallery_klass, gallery_identifier=request.GET['gallery_id'], owner=owner)

        image_klass = apps.get_model(di_settings.CONFIG['DROPIMAGE_MODEL'] or 'django_dropimages.DropimagesImage')
        di = get_object_or_404(image_klass, dropimages_gallery=gallery,
                               dropimages_original_filename=request.GET['original_filename'])
        di.delete()
        return self.render_json_response({})
