from rest_framework import serializers
from .models import *

class TuristaSerializer(serializers.ModelSerializer):
    faixa_etaria_turista = serializers.CharField(
        source='get_faixa_etaria_display',
        read_only=True
    )

    pais_turista = serializers.CharField(
        source='get_pais_display',
        read_only=True
    )

    cidade_turista = serializers.CharField(
        source='get_cidade_display',
        read_only=True
    )

    genero_turista = serializers.CharField(
        source='get_genero_display',
        read_only=True
    )

    escolaridade_turista = serializers.CharField(
        source='get_escolaridade_display',
        read_only=True
    )

    renda_estimada_turista = serializers.CharField(
        source='get_renda_estimada_display',
        read_only=True
    )
    
    estado_turista = serializers.CharField(
        source='get_estado_display',
        read_only=True
    )
    class Meta:
        model = Turista
        fields = '__all__'

class ViagemSerializer(serializers.ModelSerializer):

    motivo = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    motivo_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Motivo.objects.all(),
        source='motivo'
    )

    veiculo_utilizado = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    veiculo_utilizado_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Veiculo.objects.all(),
        source='veiculo_utilizado'
    )
    tempo_de_estadia_turista = serializers.CharField(source='get_tempo_de_estadia_display', read_only=True)
    reincidencia_turista = serializers.CharField(source='get_reincidencia_display', read_only=True)
    como_soube_dos_mirantes = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    como_soube_dos_mirantes_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=ConhecimentoMirantes.objects.all(),
        source='como_soube_dos_mirantes'
    )
    tipo_de_hospedagem = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    tipo_de_hospedagem_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=TipoHospedagem.objects.all(),
        source='tipo_de_hospedagem'
    )
    gasto_diario_estimado_turista = serializers.CharField(source='get_gasto_diario_estimado_display', read_only=True)


    class Meta:
        model = Viagem
        fields = '__all__'


class AtividadesRealizadasSerializer(serializers.ModelSerializer):
    locais_visitados = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    locais_visitados_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=LocaisVisitados.objects.all(),
        source='locais_visitados'
    )

    participacao_em_eventos = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    participacao_em_eventos_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=ParticipacaoEmEventos.objects.all(),
        source='participacao_em_eventos'
    )

    aplicativos = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    aplicativos_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=AplicativosUtilizados.objects.all(),
        source='aplicativos'
    )

    # experiencias_gastronomicas = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='title'
    # )
    # experiencias_gastronomicas_ids = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     write_only=True,
    #     queryset=ExperienciasGastronomicas.objects.all(),
    #     source='experiencias_gastronomicas'
    # )


    class Meta:
        model = AtividadesRealizadas
        fields = '__all__'

class PlanejamentoSerializer(serializers.ModelSerializer):

    antecedencia_do_planejamento_turista = serializers.CharField(
        source='get_antecedencia_do_planejamento_display',
        read_only=True
    )
    fontes_de_informacao_utilizadas = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    fontes_de_informacao_utilizadas_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=FonteInformacao.objects.all(),
        source='fontes_de_informacao_utilizadas'
    )

    forma_de_organizacao_turista = serializers.CharField(
        source='get_forma_de_organizacao_display',
        read_only=True
    )



    class Meta:
        model = Planejamento
        fields = '__all__'

class AvaliacaoSerializer(serializers.ModelSerializer):

    insatisfacao_com_a_visita = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    insatisfacao_com_a_visita_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Insatisfacao.objects.all(),
        source='insatisfacao_com_a_visita'
    )

    class Meta:
        model = Avaliacao
        fields = '__all__'


class MasterSerializer(serializers.Serializer):
    # campos de Turista
    tourist_country = serializers.ChoiceField(choices=Turista.Pais.choices)
    tourist_state = serializers.ChoiceField(choices=Turista.Estado.choices)
    tourist_city = serializers.ChoiceField(choices=Turista.Cidade.choices)
    tourist_age_group = serializers.IntegerField()
    tourist_gender = serializers.ChoiceField(choices=Turista.Genero.choices)
    tourist_education = serializers.IntegerField()
    tourist_estimated_income = serializers.ChoiceField(choices=Turista.RendaEstimada.choices)

    # PLANEJAMENTO
    planning_was_planned = serializers.BooleanField()
    planning_time = serializers.IntegerField()
    planning_information_sources = serializers.ListField(child=serializers.CharField(), allow_empty=True)
    planning_organization = serializers.CharField()

    # VIAGEM
    trip_has_reincidence = serializers.BooleanField()
    trip_reincidence = serializers.IntegerField(allow_null=True, required=False)
    trip_know_ibiapaba_mirantes = serializers.BooleanField()
    trip_how_know_ibiapaba_mirantes = serializers.ListField(child=serializers.CharField(), allow_empty=True)
    trip_reasons = serializers.ListField(child=serializers.CharField(), allow_empty=True)
    trip_vehicles = serializers.ListField(child=serializers.CharField(), allow_empty=True)
    trip_stay_time = serializers.IntegerField()
    trip_average_diary_expense = serializers.IntegerField()
    trip_hosting_types = serializers.ListField(child=serializers.CharField(), allow_empty=True)

    # ATIVIDADES
    activities_places_visited = serializers.ListField(child=serializers.CharField(), allow_empty=True)
    activities_events_visited = serializers.ListField(child=serializers.CharField(), allow_empty=True)
    activities_used_apps = serializers.ListField(child=serializers.CharField(), allow_empty=True)

    # AVALIAÇÃO
    evaluation_recommendation_rate = serializers.IntegerField()
    evaluation_dissatisfactions = serializers.ListField(child=serializers.CharField(), allow_empty=True)
    evaluation_expectation_rate = serializers.IntegerField()
    evaluation_satisfaction_rate = serializers.IntegerField()
    evaluation_return_intent_rate = serializers.IntegerField(allow_null=True, required=False)
    evaluation_open_opinion = serializers.CharField(allow_blank=True, allow_null=True)
    
    def create(self, validated_data):
        
        turista_data = {
            'pais': validated_data.pop('tourist_country'),
            'estado': validated_data.pop('tourist_state'),
            'cidade': validated_data.pop('tourist_city'),
            'faixa_etaria': validated_data.pop('tourist_age_group'),
            'genero': validated_data.pop('tourist_gender'),
            'escolaridade': validated_data.pop('tourist_education'),
            'renda_estimada': validated_data.pop('tourist_estimated_income')
        }
        
        turista = Turista.objects.create(**turista_data)

        planejamento_data = {
         'viagem_planejada'  : validated_data.pop('planning_was_planned'),
         'antecedencia_do_planejamento' : validated_data.pop('planning_time'),
         'fontes_de_informacao_utilizadas' : validated_data.pop('planning_information_sources'),
         'forma_de_organizacao' : validated_data.pop('planning_organization'),
        }
        
        planejamento = Planejamento.objects.create(**planejamento_data)

        viagem_data = {
           'ja_visitou': validated_data.pop('trip_has_reincidence'),
           'reincidencia': validated_data.pop('trip_reincidence'),
           'conhece_a_rota_mirantes': validated_data.pop('trip_know_ibiapaba_mirantes'),
           'como_soube_dos_mirantes': validated_data.pop('trip_how_know_ibiapaba_mirantes'),
           'motivo': validated_data.pop('trip_reasons'),
           'veiculo_utilizado': validated_data.pop('trip_vehicles'),
           'tempo_de_estadia' : validated_data.pop('trip_stay_time'),
           'gasto_diario_estimado': validated_data.pop('trip_average_diary_expense'),
           'tipo_de_hospedagem': validated_data.pop('trip_hosting_types')
        }
        
        viagem = Viagem.objects.create(**viagem_data)
        
        atividades_data = {
          'locais_visitados' : validated_data.pop('activities_places_visited'),
          'participacao_em_eventos' : validated_data.pop('activities_events_visited'),
          'aplicativos' : validated_data.pop('activities_used_apps')
        }
        
        atividades = AtividadesRealizadas.objects.create(**atividades_data)
        
        avaliacao_data = {
           'satisfacao_geral_com_a_visita': validated_data.pop('evaluation_recommendation_rate'),
           'insatisfacao_com_a_visita': validated_data.pop('evaluation_dissatisfactions'),
           'nivel_expectativa': validated_data.pop('evaluation_expectation_rate'),
           'nivel_satisfacao':  validated_data.pop('evaluation_satisfaction_rate'),
           'intencao_de_retorno': validated_data.pop('evaluation_return_intent_rate') ,
           'precisou_de_algum_servico': validated_data.pop('valuation_open_opinion') 
        }
        
        avaliacao = Avaliacao.objects.create(**avaliacao_data)
        