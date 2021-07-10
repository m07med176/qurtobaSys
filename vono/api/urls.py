from django.urls import path,include
from .views import GetNumbersAPI
app_name = "vono"

urlpatterns = [
    path('vono',GetNumbersAPI.as_view(),name="vono_api")
]