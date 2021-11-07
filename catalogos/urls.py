from django.urls import path
from django_rest_framework_example.api import (UserList, GroupList,
                                               UserDetails)

from .api import PaisViewSet

from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),
]

router = DefaultRouter()
router.register(r'paises', PaisViewSet, basename='paises')

urlpatterns += router.urls
