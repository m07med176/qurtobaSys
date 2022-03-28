from vcashApp.api import views as api 
from rest_framework import routers
from django.urls import path,include

router = routers.DefaultRouter()
router.register('transactions',api.TransactionsCashMVS)
router.register('sim',api.SimMVS)
router.register('sim-log',api.SimLogMVS)
router.register('device',api.DeviceMVS)
urlpatterns = [
    path('', include(router.urls)),
    path('update-coast/',api.updateCoast,name = 'update-coast'),
    path('simLogInset/',api.insertAndRemoveSim,name = 'simLogInset'),
    path('phone-list/',api.getPhoneList,name = 'phone-list')
    ]

