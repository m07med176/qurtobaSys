# ------------ API AND  APIVIEW AND VIEWSETS-----------#
# API UTILS
from rest_framework.response import Response
# VIEWSETS
from rest_framework import viewsets
# APIVIEW
from rest_framework.decorators import api_view
# ------------ SERIALIZERS -----------#
from sellersApp.api.serializers import S_SellerRecord
# ------------ MODELS -----------#
# MODELS
from sellersApp.models import SellerRecord
# ----------------------------------------------------------- #

class V_SellerRecord(viewsets.ModelViewSet):
    queryset = SellerRecord.objects.all()
    serializer_class = S_SellerRecord

# Get Raseed of Fawry limit 100
@api_view(['GET',])
def getSellerRecord(request,limit=0):
    if limit == 0:
        raseed = SellerRecord.objects.all()
    else:
        raseed = SellerRecord.objects.all()[:limit]
    serializer = S_SellerRecord(raseed, many=True)
    return Response({"results":serializer.data})
