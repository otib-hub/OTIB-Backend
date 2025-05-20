from django.db import models

# Create your models here.


class Turista(models.Model):

    pais = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    faixa_etaria = models.IntegerField()
    genero = models.CharField(max_length=150)
    escolaridade = models.CharField(max_length=150)
    renda_estimada = models.IntegerField()


class Viagem(models.Model):

    motivo_da_viagem = models.CharField(max_length=150)
    reincidencia_da_viagem = models.BooleanField(default=False)
    meio_de_transporte_utilizado = models.CharField(max_length=150)
    tempo_de_permanencia = models.IntegerField()
    tipo_de_hospedagem = models.CharField(max_length=150)
    gasto_medio_diario = models.IntegerField()
    conhece_a_rota_mirantes = models.BooleanField(default=False)

class Percepcao(models.Model):

    avaliacao_da_infra_local = models.CharField(max_length=255)
    qualidade_dos_servicos_turisticos = models.CharField(max_length=255)

class AtividadesRealizadas(models.Model):

    locais_visitados = models.CharField(max_length=255)
    participacao_em_eventos = models.CharField(max_length=255)
    experiencias_gastronomicas = models.CharField(max_length=255)


class Planejamento(models.Model):

    forma_de_organizacao = models.CharField(max_length=150)
    antecedencia_do_planejamento = models.CharField(max_length=150)
    fontes_de_informacao_utilizadas = models.CharField(max_length=150)


class Satisfacao(models.Model):

    satisfacao_geral_com_a_visita = models.CharField(max_length=150)
    insatisfacao_com_a_visita = models.CharField(max_length=150)
    intencao_de_retorno = models.IntegerField()
    recomendacao_do_destino = models.CharField(max_length=150)

class ComportamentoDigital(models.Model):

    uso_de_aplicativos_de_turismo = models.CharField(max_length=150)
    compartilhamento_de_experiencias_nas_redes_sociais = models.CharField(max_length=150)
    interacao_com_plataformas_de_avaliacao = models.CharField(max_length=150)

    viagens = models.ManyToManyField(Viagem)