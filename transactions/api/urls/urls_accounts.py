from django.urls import path
from transactions.api.controllers import accounts as api
urlpatterns = [
        # region accounts
        path('api/customerAccounts/<str:deviceNo>/',api.getAccountsCustomer),
        path('api/todayAccounts/',api.getAccountsToday),
        path('api/dateAccounts/<str:dateSelect>/',api.getAccountsDate),
        path('api/dateAndcustomerAccounts/<str:deviceNo>/<str:dateSelect>/',api.getAccountsCustomerAndDate ),
        path('api/dateFromToAccounts/<str:dateFrom>/<str:dateTo>/',api.getAccountsDateFromTo ),
        path('api/dateFromToAndcustomerAccounts/<str:deviceNo>/<str:dateFrom>/<str:dateTo>/',api.getAccountsCustomerAndDateFromTo )
        # endregion
    ]
