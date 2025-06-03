from django.contrib import admin
from .models import *


@admin.register(Viagem)
class ViagemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Viagem._meta.fields]

@admin.register(Turista)
class TuristaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Turista._meta.fields]

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Avaliacao._meta.fields]

@admin.register(AtividadesRealizadas)
class AtividadesRealizadasAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AtividadesRealizadas._meta.fields]

@admin.register(Planejamento)
class PlanejamentoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Planejamento._meta.fields]
 

@admin.register(FonteInformacao)
class FonteInformacao(admin.ModelAdmin):
    list_display = [field.name for field in FonteInformacao._meta.fields] 

@admin.register(ConhecimentoMirantes)
class ConhecimentoMirantes(admin.ModelAdmin):
    list_display = [field.name for field in ConhecimentoMirantes._meta.fields] 


@admin.register(Motivo)
class Motivo(admin.ModelAdmin):
    list_display = [field.name for field in Motivo._meta.fields] 


@admin.register(Veiculo)
class Veiculo(admin.ModelAdmin):
    list_display = [field.name for field in Veiculo._meta.fields] 


@admin.register(TipoHospedagem)
class TipoHospedagem(admin.ModelAdmin):
    list_display = [field.name for field in TipoHospedagem._meta.fields] 


@admin.register(LocaisVisitados)
class LocaisVisitados(admin.ModelAdmin):
    list_display = [field.name for field in LocaisVisitados._meta.fields] 


@admin.register(ParticipacaoEmEventos)
class ParticipacaoEmEventos(admin.ModelAdmin):
    list_display = [field.name for field in ParticipacaoEmEventos._meta.fields] 


@admin.register(AplicativosUtilizados)
class AplicativosUtilizados(admin.ModelAdmin):
    list_display = [field.name for field in AplicativosUtilizados._meta.fields]

@admin.register(Insatisfacao)
class Insatisfacao(admin.ModelAdmin):
    list_display = [field.name for field in Insatisfacao._meta.fields] 