from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from fawrySelesApp.api import views as api

from rest_framework import routers
router = routers.DefaultRouter()
router.register('raseedPortal',api.V_RassedProtal)
router.register('transactionsPortal',api.V_TransactionsPortal)


urlpatterns = [
     # api
    path('api/', include(router.urls)),
    path('api/raseedFawry/<int:limit>/',api.getRaseedOfFawry)
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
