from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Pais
from .serializers import PaisSerializer

from django.shortcuts import get_object_or_404
from rest_framework import viewsets


class PaisViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    def list(self, request):
        filter = {}
        if request.GET.get('nombre'):
            filter['nombre__icontains'] = request.GET.get('nombre')

        queryset = Pais.objects.filter(**filter).values()
        serializer = PaisSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Pais.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PaisSerializer(user)
        return Response(serializer.data)
