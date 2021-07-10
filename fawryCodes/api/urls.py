from django.urls import path,include
from fawryCodes.api import views

#-----------------------------
from fawryCodes.api.views import FawryCodesL
from rest_framework import routers
# like admin register 
router = routers.DefaultRouter()
router.register('data',FawryCodesL)
#-----------------------------

app_name = "fawryCodes"

urlpatterns = [
    path('get',views.getOnItem),
    path('update',views.updateItem),
    path('create',views.createItem),
    path('delete',views.deleteItem),
    path('', include(router.urls)),
]