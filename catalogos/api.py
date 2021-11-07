from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Pais
from .serializers import PaisSerializer


class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    # allow method for request
    # http_method_names = ['get', 'head', 'post', 'put', 'patch']

    # override methods: create, update or destroy
    # def create(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=self.request.POST)
    #
    #     if serializer.is_valid(raise_exception=True):
    #         # serializer.save()
    #
    #         return Response(
    #             serializer.validated_data, status=status.HTTP_201_CREATED
    #         )
    #
    #     return Response({
    #         'status': 'Bad request',
    #         'message': 'Account could not be created with received data.'
    #     }, status=status.HTTP_400_BAD_REQUEST)
