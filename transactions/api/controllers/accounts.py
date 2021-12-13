# region MODULE
# ------------ API -----------#
# UTILS
from rest_framework.response import Response
# APIVIEW
from rest_framework.decorators import api_view
# --------------- DATABASE MANAGER ------------------#
from databaseManager import DatabaseManager
db = DatabaseManager()
# endregion MODULE



# region ACCOUNTS
@api_view(['GET',])
def getAccountsDateFromTo(request,dateFrom,dateTo):
    return Response({"data":db.accounts(id=5,dateFrom=dateFrom,dateTo=dateTo)})

@api_view(['GET',])
def getAccountsCustomerAndDateFromTo(request,deviceNo,dateFrom,dateTo):
    return Response({"data":db.accounts(id=6,deviceNo=deviceNo,dateFrom=dateFrom,dateTo=dateTo)})

@api_view(['GET',])
def getAccountsDate(request,dateSelect):
    return Response({"data":db.accounts(id=3,dateFrom=dateSelect)})

@api_view(['GET',])
def getAccountsCustomerAndDate(request,deviceNo,dateSelect):
    return Response({"data":db.accounts(id=4,deviceNo=deviceNo,dateFrom=dateSelect)})

@api_view(['GET',])
def getAccountsCustomer(request,deviceNo):
    return Response({"data":db.accounts(id=2,deviceNo=deviceNo)})

@api_view(['GET',])
def getAccountsToday(request):
    return Response({"data":db.accounts(id=1)})
# endregion ACCOUNTS