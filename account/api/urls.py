from django.urls import path,include
from  account.api import views as api
from account.api.controllers import manager

# app_name = 'account'
# from rest_framework.authtoken.views import obtain_auth_token
#-----------------------------
from rest_framework import routers
router = routers.DefaultRouter()
router.register('',api.UsersMVS)
urlpatterns = [
    # region user crud
    # http://127.0.0.1:8000/account/api/users/
    path('users/', include(router.urls)),

    # http://127.0.0.1:8000/account/api/login/
    path('login/', api.ObtainAuthTokenView.as_view(), name="login"), 
    
    # http://127.0.0.1:8000/account/api/register/
    path('register/',api.register_account,name = "register"),
    
    # http://127.0.0.1:8000/account/api/properties/
    path('properties/', api.account_properties_view, name="properties"),

    # http://127.0.0.1:8000/account/api/properties/update/
	path('properties/update/', api.update_account_view, name="update"),

    # url: http://127.0.0.1:8000/account/api/state/<int:id>/
    path('state/<int:id>/',manager.getUserState,name = "state"),

    # url: http://127.0.0.1:8000/account/api/updateActivation/<int:id>/
    path('updateActivation/<int:id>/',manager.updateUserActivationAccountManager,name = "updateActivation"),

    # endregion user
     
    # region Customers
    # http://127.0.0.1:8000/account/api/registerManagerCustomer/
    path('registerManagerCustomer/',manager.registerAccountManagerCustomer,name = "registerManagerCustomer"), 

    # url: http://127.0.0.1:8000/account/api/deleteManagerCustomer/<int:id>/
    path('deleteManagerCustomer/<int:id>/',manager.deleteAccountManagerCustomer,name = "deleteManagerCustomer"),

    # url: http://127.0.0.1:8000/account/api/updateManagerCustomer/<int:id>/
    path('updateManagerCustomer/<int:id>/',manager.updateAccountManagerCustomer,name = "updateManagerCustomer"),
    # endregion

    # region Manager Control Users
    # url: http://127.0.0.1:8000/account/api/getManager/
    path('getManager/',manager.GetAccountManage.as_view(),name = "getManager"), 
    
    # url: http://127.0.0.1:8000/account/api/registerAccountManager/
    path('registerManager/',manager.registerAccountManager,name = "registerManager"),

    # url: http://127.0.0.1:8000/account/api/deleteManager/<int:id>/
    path('deleteManager/<int:id>/',manager.deleteAccountManager,name = "deleteManager"),

    # url: http://127.0.0.1:8000/account/api/updateManager/<int:id>/
    path('updateManager/<int:id>/',manager.updateAccountManager,name = "updateManager"),
    # endregion

    # region New Design
    # endregion New Design

    ]

