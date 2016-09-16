from django.conf.urls import url, include
import upload
from upload import views

urlpatterns = [
      url(r'^$', upload.views.request),
]