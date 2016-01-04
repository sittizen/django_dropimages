from django.views.generic import View
from braces.views import CsrfExemptMixin, JSONResponseMixin


class UploadView(CsrfExemptMixin, JSONResponseMixin, View):
    def post(self, request, *args, **kwargs):
        f = request.FILES['file']
        print args
        print kwargs
        return self.render_json_response({})
