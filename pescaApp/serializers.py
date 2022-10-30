from dataclasses import field, fields
from rest_framework import serializers
from pescaApp.models import Cuenca, Metodo, Pesca

class CuencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenca
        fields = ('id', 
                  'nombre')

class MetodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metodo
        fields = ('id', 
                  'nombre')

class PescaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesca
        fields = ('id',
                  'idCuenca',
                  'idMetodo',
                  'fecha',
                  'peso')