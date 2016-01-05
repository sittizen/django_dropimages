from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView

from .models import SomeGallery


class SomeGalleryCreateView(CreateView):
    model = SomeGallery
    template_name = 'create.html'
    fields = (
        'title',
        'dropimages_gallery',  # this field will probably be hidden in real production code
    )

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})


class SomeGalleryDetailView(DetailView):
    model = SomeGallery
    template_name = 'detail.html'
