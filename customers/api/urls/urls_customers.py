from django.urls import path
# ----------- Views ----------#
from customers.api.controllers import customers
#-----------------------------

urlpatterns = [
    
    # region customer
    # http://127.0.0.1:8000/customers/api/customers_names/
    path('api/customers_names/',customers.getCustomersNamesAndAccountsNo ),

    # http://127.0.0.1:8000/customers/api/getCustomers/
    path('api/getCustomers/',customers.GetCustomersData.as_view() ),

    # http://127.0.0.1:8000/customers/api/customers_email/<str:email>/
    path('api/customers_email/<str:email>/',customers.getCustomersByEmail),

    # http://127.0.0.1:8000/customers/api/customers_qname/<str:name>/  
    path('api/customers_qname/<str:name>/',customers.getCustomerByDeviceNoOrName), 

    # http://127.0.0.1:8000/customers/api/all_customer/  
    path('api/all_customer/',customers.getAllCustomer),

    # http://127.0.0.1:8000/customers/api/delete_customer/<str:id>/
    path('api/delete_customer/<str:id>/',customers.deleteCustomer),

    # http://127.0.0.1:8000/customers/api/areas/
    path('api/areas/',customers.getCustomersAreas),

    # http://127.0.0.1:8000/customers/api/editAreas/                   
    path('api/editAreas/',customers.editCustomersAreas),             
    # endregion customer
]

