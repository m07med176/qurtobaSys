from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
#-----------------------------
from transactions.firebase import views as firebase
from transactions.api import views as api
#-----------------------------
from rest_framework import routers
router = routers.DefaultRouter()
router.register('record',api.RecordL)
router.register('rest',api.RestL)
#-----------------------------


# root : transactions
urlpatterns = [
        # firebase
        path('' , firebase.getDataList),
        path('transactions' , firebase.getDataListEmbed , name= "transactions"),
        path('trans/<str:seller>',firebase.getMandopTrans , name ='trans' ),
        path('transApi/<str:seller>/<str:manager>',firebase.ApiView.as_view() , name ='transApi' ),
        path('office_trans/<str:manager>/<int:deviceNo>/',firebase.GetTrans.as_view() , name = 'office_trans'),
        #path('analys/<str:mandoop>' , views.analysMandop),
        #path('table',views.dataTable),      
        #path('table/<str:mandoop>',views.dataTableMandoop),        
        #path('getData',views.getDataList ,name = "getData"), 
    
        # api
        path('api/', include(router.urls)),
        path('getRest/<str:name>/',api.GetRest.as_view() , name = 'customer_rest'),
        
    ]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)


