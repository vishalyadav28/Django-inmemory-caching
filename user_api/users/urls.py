from .views import AverageAPIViewset
from rest_framework.routers import DefaultRouter
from django.urls import path,include

router=DefaultRouter()

router.register('AverageAPIViewset',AverageAPIViewset,basename='AverageAPIViewset')
urlpatterns = [
    path('check/',include(router.urls)),
    
]