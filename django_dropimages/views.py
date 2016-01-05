from django.shortcuts import get_object_or_404
from django.views.generic import View
from braces.views import CsrfExemptMixin, JSONResponseMixin

from .models import DropimagesGallery, DropimagesImage


class UploadView(CsrfExemptMixin, JSONResponseMixin, View):
    def post(self, request, *args, **kwargs):
        owner = request.user if not request.user.is_anonymous() else None
        image = request.FILES['file']
        gallery, _ = DropimagesGallery.objects.get_or_create(gallery_identifier=request.GET['gallery_id'],
                                                             owner=owner)
        DropimagesImage.objects.create(gallery=gallery, image=image, original_filename=image._name)
        return self.render_json_response({
            'gallery_identifier': request.GET['gallery_id'],
            'gallery_pk': gallery.pk,
            'file_name': image._name,
        })


class DeleteView(CsrfExemptMixin, JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        owner = request.user if not request.user.is_anonymous() else None
        gallery = get_object_or_404(DropimagesGallery, gallery_identifier=request.GET['gallery_id'], owner=owner)
        di = get_object_or_404(DropimagesImage, gallery=gallery, original_filename=request.GET['original_filename'])
        di.delete()
        return self.render_json_response({})
