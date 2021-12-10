from django.urls import path,include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
# ----------- Views ----------#
from customers.api import views as api
from customers.firebase import views as firebase
from customers.web import views as web
#-----------------------------

from rest_framework import routers
router = routers.DefaultRouter()
router.register('customers',api.Customer_infoL)
router.register('sellers',api.Mandop_InfoL)
router.register('getCustomers',api.GetCustomersData)
router.register(r'getCustomersBySeller/(?P<seller>\d+?)',api.GetCustomersDataBySeller, basename='GetCustomersDataBySeller')


#-----------------------------

urlpatterns = [
    # region WEB
    path('', web.showList,name='showList'),
    path('create/',web.createCustomer,name="create" ),
    path('update/<str:id>/',web.updateCustomer,name="updateCustomer" ),
    url(r'^read$', web.customerTable),
    url(r'^deleteCustomer/(?P<id>\d+)$', web.deleteCustomer, name='deleteCustomer'),
    # endregion WEB

    # region Firebase
    path('customers_manadeep',firebase.manadeepCustomers,name="customers_manadeep" ),
    path('customers_migrate/<str:email>',firebase.migrateCustomers,name="customers_migrate" ),
    # endregion Firebase
    
    # region customer
    path('api/customers_names/',api.getCustomersNamesAndAccountsNo ),
    path('api/customers_email/<str:email>/',api.getCustomersByEmail),
    path('api/customers_qname/<str:name>/',api.getCustomerByDeviceNoOrName),   
    path('api/all_customer/',api.getAllCustomer),
    path('api/delete_customer/<str:id>/',api.deleteCustomer),
    # endregion customer

    # region seller
    path('api/sellers_names/',api.getSellersNamesAndAccountsNo),
    path('api/sellers_qname/<str:name>/',api.getSellerByAccountNoOrName),
    path('api/all_seller/',api.getAllSellers),
    path('api/delete_seller/<str:id>/',api.deleteSeller),
    path('api/areas/',api.getCustomersAreas),                   # http://127.0.0.1:8000/customers/api/areas/
    path('api/editAreas/',api.editCustomersAreas),              # http://127.0.0.1:8000/customers/api/editAreas/
    # endregion seller

    # api
    path('api/', include(router.urls)),
    # autoComplete
    path('api/autoComplete/',api.getAllAutocompleteData),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
