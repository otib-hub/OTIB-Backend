from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from .models import *
from .serializers import * 

class TuristaListCreateView(generics.ListCreateAPIView):
    queryset = Turista.objects.all()
    serializer_class = TuristaSerializer

    permission_classes = [permissions.AllowAny]

class TuristaUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Turista.objects.all()
    serializer_class = TuristaSerializer

    permission_classes = [permissions.AllowAny]

class ViagemListCreateView(generics.ListCreateAPIView):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer

    permission_classes = [permissions.AllowAny]

class ViagemUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer

    permission_classes = [permissions.AllowAny]

class PercepcaoListCreateView(generics.ListCreateAPIView):
    queryset = Percepcao.objects.all()
    serializer_class = PercepcaoSerializer

    permission_classes = [permissions.AllowAny]

class PercepcaoUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Percepcao.objects.all()
    serializer_class = PercepcaoSerializer

    permission_classes = [permissions.AllowAny]

class AtividadesRealizadasListCreateView(generics.ListCreateAPIView):
    queryset = AtividadesRealizadas.objects.all()
    serializer_class = AtividadesRealizadasSerializer

    permission_classes = [permissions.AllowAny]

class AtividadesRealizadasUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AtividadesRealizadas.objects.all()
    serializer_class = AtividadesRealizadasSerializer

    permission_classes = [permissions.AllowAny]

class PlanejamentoListCreateView(generics.ListCreateAPIView):
    queryset = Planejamento.objects.all()
    serializer_class = PlanejamentoSerializer

    permission_classes = [permissions.AllowAny]


class PlanejamentoUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planejamento.objects.all()
    serializer_class = PlanejamentoSerializer

    permission_classes = [permissions.AllowAny]

class SatisfacaoListCreateView(generics.ListCreateAPIView):
    queryset = Satisfacao.objects.all()
    serializer_class = SatisfacaoSerializer

    permission_classes = [permissions.AllowAny]

class SatisfacaoUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Satisfacao.objects.all()
    serializer_class = SatisfacaoSerializer

    permission_classes = [permissions.AllowAny]

class ComportamentoDigitalListCreateView(generics.ListCreateAPIView):
    queryset = ComportamentoDigital.objects.all()
    serializer_class = ComportamentoDigitalSerializer

    permission_classes = [permissions.AllowAny]

class ComportamentoDigitalUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComportamentoDigital.objects.all()
    serializer_class = ComportamentoDigitalSerializer

    permission_classes = [permissions.AllowAny]

