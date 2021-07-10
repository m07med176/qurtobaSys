from django.urls import path
from fawryCodes import views
from django.conf import settings
from django.conf.urls.static import static
# root : fawryCodes
urlpatterns = [
        path('' , views.home),
    ]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
