# ------------ API AND  APIVIEW AND VIEWSETS-----------#
# API UTILS
from rest_framework.response import Response
# VIEWSETS
from rest_framework import viewsets
# APIVIEW
from rest_framework.decorators import api_view
# ------------ SERIALIZERS -----------#
from fawrySelesApp.api.serializers import S_RassedProtal,S_TransactionsPortal
# ------------ MODELS -----------#
# MODELS
from fawrySelesApp.models import RassedProtal,TransactionsPortal
# ----------------------------------------------------------- #

class V_RassedProtal(viewsets.ModelViewSet):
    queryset = RassedProtal.objects.all()
    serializer_class = S_RassedProtal

class V_TransactionsPortal(viewsets.ModelViewSet):
    queryset = TransactionsPortal.objects.all()
    serializer_class = S_TransactionsPortal

# Get Raseed of Fawry limit 100
@api_view(['GET',])
def getRaseedOfFawry(request,limit=0):
    if limit == 0:
        raseed = RassedProtal.objects.all()
    else:
        raseed = RassedProtal.objects.all()[:limit]
    serializer = S_RassedProtal(raseed, many=True)
    return Response({"results":serializer.data})
