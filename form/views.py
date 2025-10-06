from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from .models import *
from .serializers import * 

class TuristaViewSet(viewsets.ModelViewSet):
    queryset = Turista.objects.all()
    serializer_class = TuristaSerializer


class ViagemViewSet(viewsets.ModelViewSet):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class AtividadesRealizadasViewSet(viewsets.ModelViewSet):
    queryset = AtividadesRealizadas.objects.all()
    serializer_class = AtividadesRealizadasSerializer


class PlanejamentoViewSet(viewsets.ModelViewSet):
    queryset = Planejamento.objects.all()
    serializer_class = PlanejamentoSerializer




class PesquisaCompletaView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MasterSerializer(data=request.data)
        if serializer.is_valid():
            turista = serializer.save()
            turista_data = TuristaSerializer(turista).data
            return Response(turista_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

