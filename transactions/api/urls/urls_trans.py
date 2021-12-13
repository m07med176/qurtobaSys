from django.urls import path
from transactions.api.controllers import transactions as trans



# root : transactions
urlpatterns = [
        # region transactions

        # region TRANSACTIONS USER
        path('api/dateTransUser/<str:type>/<str:dateSelect>/',trans.getTransactionsDateUser ),
        path('api/userToday/',trans.getTransactionsUserToday ),
        path('api/userTransLimit/',trans.getTransactionsUserLimit ),
        
        path('api/dateFromToTransUser/<str:type>/<str:dateFrom>/<str:dateTo>/',trans.getTransactionsDateFromToUser ),
        # endregion TRANSACTIONS USER

        # region TRANSACTIONS UTILS
        path('api/todayTrans/',trans.getTransactionsToday),
        path('api/trans_rest_customer/<int:id>/',trans.getTransactionsCustomerById), 
        path('api/lastTrans/',trans.getLastDateAndTime , name ='lastTrans' ),
        # endregion
        # region DATE FILTER
        path('api/dateTrans/<str:dateSelect>/<str:type>/<int:seller>/',trans.getTransactionsDate),
        path('api/dateFromToTrans/<str:dateFrom>/<str:dateTo>/<str:type>/<int:seller>/',trans.getTransactionsDateFromTo ),
        # endregion
        # region DEVICE NO FILTER
        path('api/customerTrans/<str:deviceNo>/<str:type>/',trans.getTransactionsCustomer),
        path('api/dateAndcustomerTrans/<str:deviceNo>/<str:dateSelect>/<str:type>/',trans.getTransactionsCustomerAndDate ),
        path('api/dateFromToAndcustomerTrans/<str:deviceNo>/<str:dateFrom>/<str:dateTo>/<str:type>/',trans.getTransactionsCustomerAndDateFromTo ),
        # endregion
        
        # endregion

        
    ]
