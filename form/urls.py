from django.urls import path
from .views import *

urlpatterns = [
    path('create_turista/', TuristaListCreateView.as_view(), name = 'create-turista'),
    path('update_delete_turista/<pk>', TuristaUpdateDeleteView.as_view(), name = 'update-delete-turista'),

    path('create_viagem/', ViagemListCreateView.as_view(), name = 'create-viagem'),
    path('update_delete_viagem/<pk>', ViagemUpdateDeleteView.as_view(), name = 'update-delete-viagem'),    

    path('create_percepcao/', PercepcaoListCreateView.as_view(), name = 'create-percepcao'),
    path('update_delete_percepcao/<pk>', PercepcaoUpdateDeleteView.as_view(), name = 'update-delete-percepcao'),

    path('create_atividades_realizadas/', AtividadesRealizadasListCreateView.as_view(), name = 'create-atividades'),
    path('update_delete_atividades_realizadas/<pk>', AtividadesRealizadasUpdateDeleteView.as_view(), name = 'update-delete-atividades'),
    
    path('create_planejamento/', PlanejamentoListCreateView.as_view(), name = 'create-planejamento'),
    path('update_delete_planejamento/<pk>', PlanejamentoUpdateDeleteView.as_view(), name = 'update-delete-planejamento'),
        
    path('create_satisfacao/', SatisfacaoListCreateView.as_view(), name = 'create-satisfacao'),
    path('update_delete_satisfacao/<pk>', SatisfacaoUpdateDeleteView.as_view(), name = 'update-delete-satisfacao'),

    path('create_comportamento_digital/', ComportamentoDigitalListCreateView.as_view(), name = 'create-comportamento'),
    path('update_delete_comportamento_digital/<pk>', ComportamentoDigitalUpdateDeleteView.as_view(), name = 'update-delete-comportamento-digital'),
]