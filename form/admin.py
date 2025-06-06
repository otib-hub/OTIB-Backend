from django.contrib import admin
from .models import *
@admin.register(Viagem)
class ViagemAdmin(admin.ModelAdmin):
    # 1) Lista de colunas que queremos mostrar no changelist
    list_display = [
        'id',
        'turista',
        'ja_visitou',
        'conhece_a_rota_mirantes',
        'display_motivo',
        'display_veiculo_utilizado',
        'display_como_soube_dos_mirantes',
        'display_tipo_de_hospedagem',
        'display_tempo_de_estadia',
        'display_reincidencia',
        'display_gasto_diario_estimado',
    ]
    list_display_links = ['id', 'turista']

    def display_motivo(self, obj: Viagem):
        return ", ".join(m.title for m in obj.motivo.all())
    display_motivo.short_description = 'Motivos'      # cabeçalho na coluna
    display_motivo.admin_order_field = 'motivo'      # (opcional) permite ordering

    def display_veiculo_utilizado(self, obj: Viagem):
        return ", ".join(v.title for v in obj.veiculo_utilizado.all())
    display_veiculo_utilizado.short_description = 'Veículos'
    display_veiculo_utilizado.admin_order_field = 'veiculo_utilizado'

    def display_como_soube_dos_mirantes(self, obj: Viagem):
        return ", ".join(c.title for c in obj.como_soube_dos_mirantes.all())
    display_como_soube_dos_mirantes.short_description = 'Como soube dos Mirantes'
    display_como_soube_dos_mirantes.admin_order_field = 'como_soube_dos_mirantes'

    def display_tipo_de_hospedagem(self, obj: Viagem):
        return ", ".join(t.title for t in obj.tipo_de_hospedagem.all())
    display_tipo_de_hospedagem.short_description = 'Tipos de Hospedagem'
    display_tipo_de_hospedagem.admin_order_field = 'tipo_de_hospedagem'

    def display_tempo_de_estadia(self, obj: Viagem):
        return obj.get_tempo_de_estadia_display()
    display_tempo_de_estadia.short_description = 'Tempo de Estadia'

    def display_reincidencia(self, obj: Viagem):
        return obj.get_reincidencia_display()
    display_reincidencia.short_description = 'Reincidência'

    def display_gasto_diario_estimado(self, obj: Viagem):
        return obj.get_gasto_diario_estimado_display()
    display_gasto_diario_estimado.short_description = 'Gasto Diário Estimado'
    
@admin.register(Turista)
class TuristaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Turista._meta.fields]

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Avaliacao._meta.fields] + ['display_insatisfacao_com_a_visita']
    
    def display_insatisfacao_com_a_visita(self, obj: Planejamento):
        return ", ".join(m.title for m in obj.insatisfacao_com_a_visita.all())
    display_insatisfacao_com_a_visita.short_description = 'Insatisfação'

@admin.register(AtividadesRealizadas)
class AtividadesRealizadasAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AtividadesRealizadas._meta.fields] + ['display_locais_visitados'] + ['display_participacao_em_eventos'] + ['display_aplicativos']

    def display_locais_visitados(self, obj: Planejamento):
        return ", ".join(m.title for m in obj.locais_visitados.all())
    display_locais_visitados.short_description = 'Locais Visitados'  
     
    def display_participacao_em_eventos(self, obj: Planejamento):
        return ", ".join(m.title for m in obj.participacao_em_eventos.all())
    display_participacao_em_eventos.short_description = 'Eventos Participados'
 
    def display_aplicativos(self, obj: Planejamento):
        return ", ".join(m.title for m in obj.aplicativos.all())
    display_aplicativos.short_description = 'Aplicativos Utilizados'

@admin.register(Planejamento)
class PlanejamentoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Planejamento._meta.fields] + ['display_fontes_de_info']

    def display_fontes_de_info(self, obj: Planejamento):
        return ", ".join(m.title for m in obj.fontes_de_informacao_utilizadas.all())
    display_fontes_de_info.short_description = 'Fontes de informação utilizadas' 
    display_fontes_de_info.admin_order_field = 'fontes'  

# @admin.register(FonteInformacao)
# class FonteInformacao(admin.ModelAdmin):
#     list_display = [field.name for field in FonteInformacao._meta.fields] 

# @admin.register(ConhecimentoMirantes)
# class ConhecimentoMirantes(admin.ModelAdmin):
#     list_display = [field.name for field in ConhecimentoMirantes._meta.fields] 


# @admin.register(Motivo)
# class Motivo(admin.ModelAdmin):
#     list_display = [field.name for field in Motivo._meta.fields] 


# @admin.register(Veiculo)
# class Veiculo(admin.ModelAdmin):
#     list_display = [field.name for field in Veiculo._meta.fields] 


# @admin.register(TipoHospedagem)
# class TipoHospedagem(admin.ModelAdmin):
#     list_display = [field.name for field in TipoHospedagem._meta.fields] 


# @admin.register(LocaisVisitados)
# class LocaisVisitados(admin.ModelAdmin):
#     list_display = [field.name for field in LocaisVisitados._meta.fields] 


# @admin.register(ParticipacaoEmEventos)
# class ParticipacaoEmEventos(admin.ModelAdmin):
#     list_display = [field.name for field in ParticipacaoEmEventos._meta.fields] 


# @admin.register(AplicativosUtilizados)
# class AplicativosUtilizados(admin.ModelAdmin):
#     list_display = [field.name for field in AplicativosUtilizados._meta.fields]

# @admin.register(Insatisfacao)
# class Insatisfacao(admin.ModelAdmin):
#     list_display = [field.name for field in Insatisfacao._meta.fields] 