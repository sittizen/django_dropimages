from django.conf.urls import url


class DropImagesUrl(object):
    _urlpatterns = None

    @classmethod
    def get_urls(cls):
        if cls._urlpatterns is None:
            from . import views
            # Load URLs in a temporary variable for thread safety.
            # Global URLs
            urlpatterns = [
                url(r'^upload/$', views.UploadView.as_view(), name='upload'),
                url(r'^delete/$', views.DeleteView.as_view(), name='delete'),
            ]
            cls._urlpatterns = urlpatterns
        return cls._urlpatterns

urlpatterns = DropImagesUrl.get_urls()
