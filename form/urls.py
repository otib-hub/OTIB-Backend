from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'turista', TuristaViewSet, basename='turista')
router.register(r'viagem', ViagemViewSet, basename='viagem')
router.register(r'avaliacao', AvaliacaoViewSet, basename='avaliacao')
router.register(r'atividades-realizadas', AtividadesRealizadasViewSet, basename='atividades-realizadas')
router.register(r'planejamento', PlanejamentoViewSet, basename='planejamento')


urlpatterns = [
 path('', include(router.urls)),
]