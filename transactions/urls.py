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
    
        #---| api |---#
        path('api/', include(router.urls)),
        path('api/getRest/<str:name>/',api.GetRest.as_view()),
        # seller should pay
        path('restSeller/<str:email>/',api.getSellerRest),
        path('api/getAllRest/',api.getAllRest ),

        # transactions
        path('api/customerTrans/<str:deviceNo>/',api.getTransactionsCustomer),# 
        path('api/trans_rest_customer/<int:id>/',api.getTransactionsCustomerById),# 

        path('api/todayTrans/',api.getTransactionsToday),
        path('api/dateTrans/<str:dateSelect>/',api.getTransactionsDate),
        path('api/dateAndcustomerTrans/<str:deviceNo>/<str:dateSelect>/',api.getTransactionsCustomerAndDate ),
        path('api/dateFromToTrans/<str:dateFrom>/<str:dateTo>/',api.getTransactionsDateFromTo ),
        path('api/dateFromToAndcustomerTrans/<str:deviceNo>/<str:dateFrom>/<str:dateTo>/',api.getTransactionsCustomerAndDateFromTo ),

        path('api/lastTrans/',api.getLastDateAndTime , name ='lastTrans' ),
        # accounts
        path('api/customerAccounts/<str:deviceNo>/',api.getAccountsCustomer),
        path('api/todayAccounts/',api.getAccountsToday),
        path('api/dateAccounts/<str:dateSelect>/',api.getAccountsDate),
        path('api/dateAndcustomerAccounts/<str:deviceNo>/<str:dateSelect>/',api.getAccountsCustomerAndDate ),
        path('api/dateFromToAccounts/<str:dateFrom>/<str:dateTo>/',api.getAccountsDateFromTo ),
        path('api/dateFromToAndcustomerAccounts/<str:deviceNo>/<str:dateFrom>/<str:dateTo>/',api.getAccountsCustomerAndDateFromTo )
    ]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
