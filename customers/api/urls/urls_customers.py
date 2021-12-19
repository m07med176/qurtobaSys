from django.urls import path
# ----------- Views ----------#
from customers.api.controllers import customers
#-----------------------------

urlpatterns = [
    
    # region customer
    path('api/customers_names/',customers.getCustomersNamesAndAccountsNo ),
    path('api/customers_email/<str:email>/',customers.getCustomersByEmail),
    path('api/customers_qname/<str:name>/',customers.getCustomerByDeviceNoOrName),   
    path('api/all_customer/',customers.getAllCustomer),
    path('api/delete_customer/<str:id>/',customers.deleteCustomer),
    path('api/areas/',customers.getCustomersAreas),                   # http://127.0.0.1:8000/customers/api/areas/
    path('api/editAreas/',customers.editCustomersAreas),              # http://127.0.0.1:8000/customers/api/editAreas/
    # endregion customer
]

