from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
                path('', views.login,name='login'), # root
                path('home' , views.home ,name = 'home'),
                
                ]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
#urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)