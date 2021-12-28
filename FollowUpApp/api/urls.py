from django.urls import path,include
from FollowUpApp.api import views
# -------------------------------------
from rest_framework import routers
router = routers.DefaultRouter()
router.register('',views.FollowUpMVS)

urlpatterns = [
    # http://127.0.0.1:8000/follow/api/router/
    path('router/', include(router.urls)),
    # http://127.0.0.1:8000/follow/api/startDay/
    path('startDay/', views.startDay),
    # http://127.0.0.1:8000/follow/api/endDay/
    path('endDay/', views.endDay),
    # http://127.0.0.1:8000/follow/api/addNotes/
    path('addNotes/', views.addNotes),
    # http://127.0.0.1:8000/follow/api/addTransport/
    path('addTransport/', views.addTransport),

    ]

