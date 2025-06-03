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

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    permission_classes = [permissions.AllowAny]

class AtividadesRealizadasViewSet(viewsets.ModelViewSet):
    queryset = AtividadesRealizadas.objects.all()
    serializer_class = AtividadesRealizadasSerializer

    permission_classes = [permissions.AllowAny]

class PlanejamentoViewSet(viewsets.ModelViewSet):
    queryset = Planejamento.objects.all()
    serializer_class = PlanejamentoSerializer

    permission_classes = [permissions.AllowAny]

   
