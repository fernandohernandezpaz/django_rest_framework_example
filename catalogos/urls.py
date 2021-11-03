from django.contrib import admin
from django.urls import path, include
from .api import PaisViewSet
from .views import get_paises

urlpatterns = [
    path('paises/', PaisViewSet.as_view({'get': 'list'}), name='api-paises'),
    path('web/paises/', get_paises, name='web-paises'),
]
