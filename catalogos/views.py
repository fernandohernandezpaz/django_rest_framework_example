from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import PaisSerializer
from .models import Pais


# Create your views here.

@csrf_exempt
def get_paises(request):
    filter = {}
    if request.GET.get('nombre'):
        filter['nombre__icontains'] = request.GET.get('nombre')
    queryset = Pais.objects.filter(**filter).values()
    serializer = PaisSerializer(queryset, many=True)
    return JsonResponse(serializer.data,  safe=False)
