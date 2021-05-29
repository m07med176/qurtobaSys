from django.urls import path,include
from customers import views
from django.conf.urls import url

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

    # api
     path('api/', include(router.urls)),
]
