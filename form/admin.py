from django.contrib import admin
from .models import *


@admin.register(Viagem)
class ViagemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Viagem._meta.fields]

@admin.register(Turista)
class TuristaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Turista._meta.fields]

@admin.register(Percepcao)
class PercepcaoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Percepcao._meta.fields]

@admin.register(AtividadesRealizadas)
class AtividadesRealizadasAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AtividadesRealizadas._meta.fields]

@admin.register(Planejamento)
class PlanejamentoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Planejamento._meta.fields]

@admin.register(Satisfacao)
class SatisfacaoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Satisfacao._meta.fields]

@admin.register(ComportamentoDigital)
class ComportamentoDigitalAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ComportamentoDigital._meta.fields] + ['get_viagens_ids']
   
    @admin.display(description='Viagens (IDs)')
    def get_viagens_ids(self, obj):
        return ", ".join(str(c.id) for c in obj.viagens.all())