from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from sellersApp.api import views as api
from rest_framework import routers
router = routers.DefaultRouter()
router.register('sellerRecord',api.V_SellerRecord)



urlpatterns = [
     # api
    path('api/', include(router.urls)),
    path('api/getSellerRecord/<int:limit>/',api.getSellerRecord)
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
