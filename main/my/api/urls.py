from rest_framework.routers import DefaultRouter
from my.api import views
from django.urls import path,include
router=DefaultRouter()
router.register("crud",views.crud,basename="api")

urlpatterns = [
    path('',include(router.urls)),
    path("auth/",include("rest_framework.urls"))
    
]

