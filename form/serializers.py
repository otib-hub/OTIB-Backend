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

class PercepcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Percepcao
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

class SatisfacaoSerializer(serializers.ModelSerializer):

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
        model = Satisfacao
        fields = '__all__'

class ComportamentoDigitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComportamentoDigital
        fields = '__all__'