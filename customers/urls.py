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
# like admin register 
router = routers.DefaultRouter()
router.register('customers',api.Customer_infoL)
router.register('sellers',api.Mandop_InfoL)
# router.register('accounts',api.Customer_accountL)

#-----------------------------

urlpatterns = [
    # web
    path('', web.showList,name='showList'),
    path('create/',web.createCustomer,name="create" ),
    path('update/<str:id>/',web.updateCustomer,name="updateCustomer" ),
    url(r'^read$', web.customerTable),
    url(r'^deleteCustomer/(?P<id>\d+)$', web.deleteCustomer, name='deleteCustomer'),

    # firebase
    path('customers_manadeep',firebase.manadeepCustomers,name="customers_manadeep" ),
    path('customers_migrate/<str:email>',firebase.migrateCustomers,name="customers_migrate" ),
    
    # api
    path('api/', include(router.urls)),

    # customer
    path('api_customer/',api.GetCustomersData.as_view() ),
    path('api/customers_names/',api.getCustomersNamesAndAccountsNo ),
    path('api/customers_areas/',api.getCustomersAreas),
    path('api/customers_qname/<str:name>/',api.getCustomerByDeviceNoOrName),
    

    # seller
    path('api/sellers_names/',api.getSellersNamesAndAccountsNo),
    path('api/sellers_areas/',api.getSellersAreas),
    path('api/sellers_qname/<str:name>/',api.getSellerByAccountNoOrName),
    path('api/delete_seller/<str:id>/',api.deleteSeller),
    
    path('api/autoComplete/',api.getAllAutocompleteData),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
