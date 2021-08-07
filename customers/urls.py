from django.urls import path,include
from customers import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

#-----------------------------
from .views import Customer_infoL
from rest_framework import routers
# like admin register 
router = routers.DefaultRouter()
router.register('data',Customer_infoL)
#-----------------------------

urlpatterns = [
    path('', views.showList,name='showList'),
    path('create/',views.createCustomer,name="create" ),
    path('update/<str:id>/',views.updateCustomer,name="updateCustomer" ),
    url(r'^read$', views.customerTable),
    url(r'^deleteCustomer/(?P<id>\d+)$', views.deleteCustomer, name='deleteCustomer'),

    # manadeep customers
    path('customers_manadeep',views.manadeepCustomers,name="customers_manadeep" ),
    path('customers_migrate/<str:email>',views.migrateCustomers,name="customers_migrate" ),
    
    # api
    path('api/', include(router.urls)),
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
