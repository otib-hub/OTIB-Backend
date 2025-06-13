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
    tourist_country = serializers.CharField()
    tourist_state = serializers.CharField()
    tourist_city = serializers.CharField()
    tourist_age_group = serializers.IntegerField()
    tourist_gender = serializers.ChoiceField(choices=Turista.Genero.choices)
    tourist_education = serializers.IntegerField()
    tourist_estimated_income = serializers.ChoiceField(choices=Turista.RendaEstimada.choices)

    planning_was_planned = serializers.BooleanField()
    planning_time = serializers.IntegerField(allow_null=True,  required=False,)
    planning_information_sources = serializers.ListField(
        child=serializers.CharField(), allow_empty=True,  required=False
    )
    planning_organization = serializers.IntegerField()

    trip_has_reincidence = serializers.BooleanField()
    trip_reincidence = serializers.IntegerField(allow_null=True, required=False)
    trip_know_ibiapaba_mirantes = serializers.BooleanField()
    trip_how_know_ibiapaba_mirantes = serializers.ListField(
        child=serializers.CharField(), allow_empty=True,  required=False,
    ) 
    trip_reasons = serializers.ListField(child=serializers.CharField(), allow_empty=True)  # IDs ou títulos de Motivo
    trip_vehicles = serializers.ListField(child=serializers.CharField(), allow_empty=True)  # IDs ou títulos de Veiculo
    trip_stay_time = serializers.IntegerField()
    trip_average_diary_expense = serializers.IntegerField()
    trip_hosting_types = serializers.ListField(
        child=serializers.CharField(), allow_empty=True
    )

    activities_cities_visited = serializers.ListField(
        child=serializers.CharField(), allow_empty=True
    )
    activities_attractions_visited = serializers.ListField(
        child=serializers.CharField(), allow_empty=True
    )
    activities_used_apps = serializers.ListField(
        child=serializers.CharField(), allow_empty=True,  required=False,
    )

    evaluation_recommendation_rate = serializers.IntegerField()
    evaluation_dissatisfactions = serializers.ListField(
        child=serializers.CharField(), allow_empty=True,  required=False,
    )
    evaluation_expectation_rate = serializers.IntegerField()
    evaluation_satisfaction_rate = serializers.IntegerField()
    evaluation_return_intent_rate = serializers.IntegerField(allow_null=True, required=False)
    evaluation_open_opinion = serializers.CharField(allow_blank=True, allow_null=True)

    def _set_m2m_field(self, instance, field_name, raw_list, related_model, error_key):
        try:
            ids = [int(x) for x in raw_list]
            qs = related_model.objects.filter(id__in=ids)
            missing = set(ids) - set(qs.values_list('id', flat=True))
            if missing:
                raise serializers.ValidationError({error_key: f"IDs inválidos em {related_model.__name__}: {sorted(missing)}"})
            instance.__getattribute__(field_name).set(qs)
            return
        except (ValueError, TypeError):
            # 2) Caso não sejam IDs válidos, interpreta como títulos
            qs = related_model.objects.filter(title__in=raw_list)
            missing_titles = set(raw_list) - set(qs.values_list('title', flat=True))
            if missing_titles:
                raise serializers.ValidationError({error_key: f"Títulos inválidos em {related_model.__name__}: {sorted(missing_titles)}"})
            instance.__getattribute__(field_name).set(qs)
            return

    def create(self, validated_data):
        turista_data = {
            "pais": validated_data.pop("tourist_country"),
            "estado": validated_data.pop("tourist_state"),
            "cidade": validated_data.pop("tourist_city"),
            "faixa_etaria": validated_data.pop("tourist_age_group"),
            "genero": validated_data.pop("tourist_gender"),
            "escolaridade": validated_data.pop("tourist_education"),
            "renda_estimada": validated_data.pop("tourist_estimated_income"),
        }
        turista = Turista.objects.create(**turista_data)

        fontes_raw = validated_data.pop("planning_information_sources", [])
        planejamento = Planejamento.objects.create(
            turista=turista,
            viagem_planejada=validated_data.pop("planning_was_planned"),
            antecedencia_do_planejamento=validated_data.pop("planning_time",0),
            forma_de_organizacao=validated_data.pop("planning_organization"),
        )
        self._set_m2m_field(
            instance=planejamento,
            field_name="fontes_de_informacao_utilizadas",
            raw_list=fontes_raw,
            related_model=FonteInformacao,
            error_key="planning_information_sources",
        )
        
        motivos_raw = validated_data.pop("trip_reasons")
        veiculos_raw = validated_data.pop("trip_vehicles")
        conhecimentos_raw = validated_data.pop("trip_how_know_ibiapaba_mirantes",[])
        hospedagens_raw = validated_data.pop("trip_hosting_types")

        viagem = Viagem.objects.create(
            turista=turista,
            ja_visitou=validated_data.pop("trip_has_reincidence"),
            reincidencia=validated_data.pop("trip_reincidence",0),
            conhece_a_rota_mirantes=validated_data.pop("trip_know_ibiapaba_mirantes",),
            tempo_de_estadia=validated_data.pop("trip_stay_time"),
            gasto_diario_estimado=validated_data.pop("trip_average_diary_expense"),
        )
        self._set_m2m_field(
            instance=viagem,
            field_name="motivo",
            raw_list=motivos_raw,
            related_model=Motivo,
            error_key="trip_reasons",
        )
        self._set_m2m_field(
            instance=viagem,
            field_name="veiculo_utilizado",
            raw_list=veiculos_raw,
            related_model=Veiculo,
            error_key="trip_vehicles",
        )
        self._set_m2m_field(
            instance=viagem,
            field_name="como_soube_dos_mirantes",
            raw_list=conhecimentos_raw,
            related_model=ConhecimentoMirantes,
            error_key="trip_how_know_ibiapaba_mirantes",
        )
        self._set_m2m_field(
            instance=viagem,
            field_name="tipo_de_hospedagem",
            raw_list=hospedagens_raw,
            related_model=TipoHospedagem,
            error_key="trip_hosting_types",
        )

        locais_raw = validated_data.pop("activities_cities_visited")
        eventos_raw = validated_data.pop("activities_attractions_visited")
        apps_raw = validated_data.pop("activities_used_apps",[])

        atividades = AtividadesRealizadas.objects.create(turista=turista)
        self._set_m2m_field(
            instance=atividades,
            field_name="locais_visitados",
            raw_list=locais_raw,
            related_model=LocaisVisitados,
            error_key="activities_cities_visited",
        )
        self._set_m2m_field(
            instance=atividades,
            field_name="participacao_em_eventos",
            raw_list=eventos_raw,
            related_model=ParticipacaoEmEventos,
            error_key="activities_attractions_visited",
        )
        self._set_m2m_field(
            instance=atividades,
            field_name="aplicativos",
            raw_list=apps_raw,
            related_model=AplicativosUtilizados,
            error_key="activities_used_apps",
        )

        dissat_raw = validated_data.pop("evaluation_dissatisfactions",[])
        avaliacao = Avaliacao.objects.create(
            turista=turista,
            satisfacao_geral_com_a_visita=validated_data.pop("evaluation_recommendation_rate"),
            nivel_expectativa=validated_data.pop("evaluation_expectation_rate"),
            nivel_satisfacao=validated_data.pop("evaluation_satisfaction_rate"),
            intencao_de_retorno=validated_data.pop("evaluation_return_intent_rate", None),
            precisou_de_algum_servico=validated_data.pop("evaluation_open_opinion"),
        )
        self._set_m2m_field(
            instance=avaliacao,
            field_name="insatisfacao_com_a_visita",
            raw_list=dissat_raw,
            related_model=Insatisfacao,
            error_key="evaluation_dissatisfactions",
        )

        return turista