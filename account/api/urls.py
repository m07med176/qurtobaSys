from django.urls import path,include
from  account.api import views as api
# app_name = 'account'
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
router = routers.DefaultRouter()
router.register('users',api.UsersMVS)
urlpatterns = [
    # api
    path('router/', include(router.urls)),
    path('register/',api.register_account),
    path('registerManager/',api.registerAccountManager),
    path('updateManager/<int:id>/',api.updateAccountManager),
    path('deleteManager/<int:id>/',api.deleteAccountManager),
    path('getManager/',api.getAccountManager),
    path('login/', api.ObtainAuthTokenView.as_view(), name="login"), 
    path('properties', api.account_properties_view, name="properties"),
	path('properties/update/', api.update_account_view, name="update"),
    path('state/<int:id>/',api.getUserState)
]