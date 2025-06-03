from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from .models import *
from .serializers import * 

class TuristaViewSet(viewsets.ModelViewSet):
    queryset = Turista.objects.all()
    serializer_class = TuristaSerializer

    permission_classes = [permissions.AllowAny]

class ViagemViewSet(viewsets.ModelViewSet):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer

    permission_classes = [permissions.AllowAny]

class PercepcaoViewSet(viewsets.ModelViewSet):
    queryset = Percepcao.objects.all()
    serializer_class = PercepcaoSerializer

    permission_classes = [permissions.AllowAny]

class AtividadesRealizadasViewSet(viewsets.ModelViewSet):
    queryset = AtividadesRealizadas.objects.all()
    serializer_class = AtividadesRealizadasSerializer

    permission_classes = [permissions.AllowAny]

class PlanejamentoViewSet(viewsets.ModelViewSet):
    queryset = Planejamento.objects.all()
    serializer_class = PlanejamentoSerializer

    permission_classes = [permissions.AllowAny]

class SatisfacaoViewSet(viewsets.ModelViewSet):
    queryset = Satisfacao.objects.all()
    serializer_class = SatisfacaoSerializer

    permission_classes = [permissions.AllowAny]

class ComportamentoDigitalViewSet(viewsets.ModelViewSet):
    queryset = ComportamentoDigital.objects.all()
    serializer_class = ComportamentoDigitalSerializer

    permission_classes = [permissions.AllowAny]

   
