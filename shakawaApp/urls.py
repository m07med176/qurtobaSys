from django.urls import path,include

urlpatterns = [
    path('api/', include('shakawaApp.api.urls')),
    path('', include('shakawaApp.web.urls')),
]