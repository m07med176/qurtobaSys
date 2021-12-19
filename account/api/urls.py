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
    # user crud
    path('users/', include(router.urls)),
    path('register/',api.register_account),
    path('login/', api.ObtainAuthTokenView.as_view(), name="login"), 
    path('properties/', api.account_properties_view, name="properties"),
	path('properties/update/', api.update_account_view, name="update"),

        # region General    
    # url: http://127.0.0.1:8000/account/api/state/<int:id>/
    path('state/<int:id>/',manager.getUserState),

    # url: http://127.0.0.1:8000/account/api/updateActivation/<int:id>/
    path('updateActivation/<int:id>/',manager.updateUserActivationAccountManager),

    # url: http://127.0.0.1:8000/account/api/getManager/
    path('getManager/',manager.GetAccountManage.as_view()), 
    # endregion General
    
    # region Customers
    # http://127.0.0.1:8000/account/api/registerManagerCustomer/
    path('registerManagerCustomer/',manager.registerAccountManagerCustomer), 

    # url: http://127.0.0.1:8000/account/api/deleteManager/<int:id>/
    path('deleteManagerCustomer/<int:id>/',manager.deleteAccountManagerCustomer),

    # url: http://127.0.0.1:8000/account/api/updateManager/<int:id>/
    path('updateManagerCustomer/<int:id>/',manager.updateAccountManagerCustomer),
    # endregion

    # region Users
    # url: http://127.0.0.1:8000/account/api/registerAccountManager/
    path('registerManager/',manager.registerAccountManager),

    # url: http://127.0.0.1:8000/account/api/deleteManager/<int:id>/
    path('deleteManager/<int:id>/',manager.deleteAccountManager),


    # url: http://127.0.0.1:8000/account/api/updateManager/<int:id>/
    path('updateManager/<int:id>/',manager.updateAccountManager),
    # endregion

    ]

