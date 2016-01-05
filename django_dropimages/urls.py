from django.conf.urls import url
import views

urlpatterns = [
    url(r'^upload/$', views.UploadView.as_view(), name='upload'),
    url(r'^delete/$', views.DeleteView.as_view(), name='delete'),
]
