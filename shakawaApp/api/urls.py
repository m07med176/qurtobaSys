from django.urls import path,include
from  shakawaApp.api import views as api
# app_name = 'account'
# from rest_framework.authtoken.views import obtain_auth_token
#-----------------------------
from rest_framework import routers
router = routers.DefaultRouter()
router.register('',api.ShakawaMVS)
urlpatterns = [
    path('router/', include(router.urls)),
    path('getShakawa/',api.getShakawa ),

]