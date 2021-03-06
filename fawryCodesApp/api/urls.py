from django.urls import path,include
from fawryCodesApp.api import views

#-----------------------------
from fawryCodesApp.api.views import FawryCodesMVS
from rest_framework import routers
# like admin register 
router = routers.DefaultRouter()
router.register('data',FawryCodesMVS)
#-----------------------------

app_name = "fawryCodes"

urlpatterns = [
    path('get',views.getOnItem),
    path('update',views.updateItem),
    path('create',views.createItem),
    path('delete',views.deleteItem),
    path('api/', include(router.urls)),
]