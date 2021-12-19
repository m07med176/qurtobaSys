# region Models
# ----------- Django ----------#
from django.urls import path,include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
# ----------- Views ----------#
from customers.api import views as api
from customers.firebase import views as firebase
from customers.web import views as web
from customers.api.urls import urls_customers,urls_sellers
from customers.api.controllers import customers,sellers
# endregion

# region Routers
from rest_framework import routers
router = routers.DefaultRouter()
router.register('customers',customers.Customer_infoL)
router.register(r'getCustomersBySeller/(?P<seller>\d+?)',customers.GetCustomersDataBySeller, basename='GetCustomersDataBySeller')

router.register('sellers',sellers.Mandop_InfoL)
# endregion

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

    # api
    path('api/', include(router.urls)),
    # autoComplete
    path('api/autoComplete/',api.getAllAutocompleteData),
]

urlpatterns +=urls_sellers.urlpatterns
urlpatterns +=urls_customers.urlpatterns
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
