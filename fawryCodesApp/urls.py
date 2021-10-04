from django.urls import path
from fawryCodesApp.web import views as web
from django.conf import settings
from django.conf.urls.static import static
# root : fawryCodes
urlpatterns = [
        path('' , web.home),
    ]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
