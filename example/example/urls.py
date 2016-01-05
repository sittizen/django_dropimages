from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from app.views import SomeGalleryCreateView, SomeGalleryDetailView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^create/$', SomeGalleryCreateView.as_view()),
    url(r'^detail/(?P<pk>\d+)/$', SomeGalleryDetailView.as_view(), name='detail'),
    url(r'^admin/', include(admin.site.urls)),
]
