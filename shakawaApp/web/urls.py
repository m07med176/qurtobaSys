from django.urls import path

from shakawaApp.web.views import (home)

app_name = 'shakawaApp'

urlpatterns = [
	path('',home,name= "home"),
]