from rest_framework import serializers
from .models import *

class TuristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turista
        fields = '__all__'

class ViagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viagem
        fields = '__all__'

class PercepcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Percepcao
        fields = '__all__'

class AtividadesRealizadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtividadesRealizadas
        fields = '__all__'

class PlanejamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planejamento
        fields = '__all__'

class SatisfacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Satisfacao
        fields = '__all__'

class ComportamentoDigitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComportamentoDigital
        fields = '__all__'