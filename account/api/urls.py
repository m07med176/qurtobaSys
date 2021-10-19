from django.urls import path
from  account.api import views as api
# app_name = 'account'
# from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('register/',api.register_account),
    path('login/', api.ObtainAuthTokenView.as_view(), name="login"), 
    path('properties', api.account_properties_view, name="properties"),
	path('properties/update', api.update_account_view, name="update"),
]