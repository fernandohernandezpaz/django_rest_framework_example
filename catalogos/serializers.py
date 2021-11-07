from .models import Pais, Curso
from rest_framework import serializers


class PaisSerializer(serializers.ModelSerializer):

    activo = serializers.BooleanField(default=True)

    class Meta:
        model = Pais
        fields = '__all__'

    # def create(self, validated_data):
    #     pais = Pais.objects.create(**validated_data)
    #     return pais
