from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from vono.models import VodafoneNumber
from .serializers import VodafoneNumberSer
class GetNumbersAPI(ListAPIView):
    queryset = VodafoneNumber.objects.all()
    serializer_class = VodafoneNumberSer
    pagination_class = PageNumberPagination