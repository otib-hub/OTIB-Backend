from django.db import models

# Create your models here.

#Turista
class Turista(models.Model):

    class FaixaEtaria(models.IntegerChoices):
        DE_18_A_24 = 1, '18 a 24 anos'
        DE_25_A_34 = 2, '25 a 34 anos'
        DE_35_A_44 = 3, '35 a 44 anos'
        DE_45_A_54 = 4, '45 a 54 anos'
        DE_55_A_64 = 5, '55 a 64 anos'
        MAIS_DE_65 = 6, '65 anos ou mais'
#alterar
  

    class Genero(models.TextChoices):
        HOMEM = 'male','Masculino'
        MULHER = 'female','Feminino'
        NAO_BINARIO = 'non_binary','Não binário'
        OUTRO = 'other','Outro'
        OMITIR = 'omit','Prefiro nao informar'

    class Escolaridade(models.IntegerChoices):
        FUNDAMENTAL_INCOMPLETO    = 1, 'Ensino fundamental incompleto'
        FUNDAMENTAL_COMPLETO      = 2, 'Ensino fundamental completo'
        MEDIO_INCOMPLETO          = 3, 'Ensino médio incompleto'
        MEDIO_COMPLETO            = 4, 'Ensino médio completo'
        SUPERIOR_INCOMPLETO       = 5, 'Ensino superior incompleto'
        SUPERIOR_COMPLETO         = 6, 'Ensino superior completo'
        ESPECIALIZACAO            = 7, 'Especialização'
        MBA                       = 8, 'MBA'
        MESTRADO                  = 9, 'Mestrado'
        DOUTORADO                 = 10, 'Doutorado'
        POS_DOUTORADO             = 11, 'Pós-doutorado'

    class RendaEstimada(models.TextChoices):
        LOW        = 'low',      'Menos de R$1.000'
        LOW_MID    = 'low_mid',  'R$1.000 - R$3.000'
        MID        = 'mid',      'R$3.000 - R$5.000'
        HIGH_MID   = 'high_mid', 'R$5.000 - R$10.000'
        HIGH       = 'high',     'Mais de R$10.000'
        OMIT       = 'omit',     'Prefiro não informar'

    data_resposta = models.DateTimeField(auto_now_add=True)
    
    pais = models.CharField(max_length=255)

    estado = models.CharField(max_length=255)
    
    cidade = models.CharField(max_length=255)

    faixa_etaria = models.IntegerField(
        choices=FaixaEtaria.choices,
        verbose_name='faixa etária'
)

    genero = models.CharField(max_length=50,
    choices=Genero.choices,
    verbose_name='genero'
    )

    escolaridade = models.IntegerField(
        choices=Escolaridade.choices,
        verbose_name='escolaridade do turista'
    )
    renda_estimada = models.CharField(
        max_length=10,
        choices=RendaEstimada.choices,
        verbose_name='renda estimada'
    )

#Viagem

class ConhecimentoMirantes(models.Model):
    title = models.CharField(max_length=150,        blank=True,
        null=True)


    def __str__(self):
        return self.title
 
class Motivo(models.Model):
    title = models.CharField(max_length=150)


    def __str__(self):
        return self.title

class Veiculo(models.Model):
    title = models.CharField(max_length=150)


    def __str__(self):
        return self.title

class TipoHospedagem(models.Model):
    title = models.CharField(max_length=150)


    def __str__(self):
        return self.title

class Viagem(models.Model):
    turista = models.ForeignKey(
        Turista,
        on_delete=models.CASCADE,
        related_name='viagens'
    )


    class TempoEstadia(models.IntegerChoices):
        UM_DIA = 1, '1 dia'
        DOIS_TRES_DIAS = 2, '2 a 3 dias'
        FIM_DE_SEMANA = 3, 'Apenas no final de semana'
        QUATRO_DIAS = 4, '4 dias'
        CINCO_DIAS = 5, '5 dias'
        UMA_SEMANA = 6, '1 semana'
        QUINZE_DIAS = 7, '15 dias'
        MAIS_QUINZE = 8, 'Mais de 15 dias'

    class Reincidencia(models.IntegerChoices):
        NULL = 0, 'Não informado'
        DUAS_A_CINCO = 1, 'Visitei entre 2 e 5 vezes'
        CINCO_A_DEZ = 2, 'Visitei entre 5 e 10 vezes'
        MAIS_DE_DEZ = 3, 'Visitei mais de 10 vezes'
        MENSAL = 4, 'Visito uma vez por mês'
        FIM_DE_SEMANA_FREQ = 5, 'Visito a cada fim de semana'



    class GastoDiario(models.IntegerChoices):
        ATE_300 = 1, 'Até R$ 300,00'
        DE_300_A_500 = 2, 'De R$ 300,00 a R$ 500,00'
        DE_500_A_1000 = 3, 'De R$ 500,00 a R$ 1.000,00'
        DE_1000_A_1500 = 4, 'De R$ 1.000,00 a R$ 1.500,00'
        DE_1500_A_2000 = 5, 'De R$ 1.500,00 a R$ 2.000,00'
        DE_2000_A_3000 = 6, 'De R$ 2.000,00 a R$ 3.000,00'
        DE_3000_A_5000 = 7, 'De R$ 3.000,00 a R$ 5.000,00'
        MAIS_5000 = 8, 'Acima de R$ 5.000,00'

    ja_visitou = models.BooleanField(default=False)
    conhece_a_rota_mirantes = models.BooleanField(default=False)
    motivo = models.ManyToManyField(Motivo)
    veiculo_utilizado = models.ManyToManyField(Veiculo)
    tempo_de_estadia = models.IntegerField(choices=TempoEstadia.choices)
    reincidencia = models.IntegerField(choices=Reincidencia.choices,        blank=True,
        null=True)
    como_soube_dos_mirantes = models.ManyToManyField(ConhecimentoMirantes)
    tipo_de_hospedagem = models.ManyToManyField(TipoHospedagem)
    gasto_diario_estimado = models.IntegerField(choices=GastoDiario.choices)



#atividades realizadas

class LocaisVisitados(models.Model):
    title = models.CharField(max_length=150)


    def __str__(self):
        return self.title

class ParticipacaoEmEventos(models.Model):
    title = models.CharField(max_length=150)


    def __str__(self):
        return self.title

class AplicativosUtilizados(models.Model):
    title = models.CharField(max_length=150,        blank=True,
        null=True)


    def __str__(self):
        return self.title

class AtividadesRealizadas(models.Model):
    turista = models.ForeignKey(
        Turista,
        on_delete=models.CASCADE,
        related_name='atividadesRealizadas'
    )
    locais_visitados = models.ManyToManyField(LocaisVisitados)
    participacao_em_eventos = models.ManyToManyField(ParticipacaoEmEventos)
    aplicativos = models.ManyToManyField(AplicativosUtilizados)




#planejamento
class FonteInformacao(models.Model):
    title = models.CharField(max_length=30,        blank=True,
        null=True)


    def __str__(self):
        return self.title

class Planejamento(models.Model):
    turista = models.ForeignKey(
        Turista,
        on_delete=models.CASCADE,
        related_name='planejamentos'
    )
    class Antecedencia(models.IntegerChoices):
        NULL = 0, 'Não informado'
        MENOS_DE_1_MES  = 1, 'Menos de 1 mês'
        UM_A_3_MESES    = 2, '1 a 3 meses'
        TRES_A_6_MESES  = 3, '3 a 6 meses'
        MAIS_DE_6_MESES = 4, 'Mais de 6 meses'


    class Organizacao(models.IntegerChoices):

        VIAGEM_INDIVIDUAL   = 1, 'Viagem individual'
        VIAGEM_EM_CASAL = 2, 'Viagem em casal'
        VIAGEM_EM_FAMILIA   = 3, 'Viagem em família'
        VIAGEM_EM_GRUPO = 4, 'Viagem em grupo'
        COM_AGENCIA_DE_VIAGENS  = 5, 'Com agência de viagens'
        OUTRO   = 6, 'Outro'


    viagem_planejada = models.BooleanField(default=False)
    antecedencia_do_planejamento = models.IntegerField(
        choices=Antecedencia.choices,
        verbose_name='antecedência do planejamento',
        blank=True,
        null=True,
    )
    
    fontes_de_informacao_utilizadas = models.ManyToManyField(FonteInformacao)

    forma_de_organizacao = models.IntegerField(
        choices=Organizacao.choices,
        verbose_name='forma de organização'
    )



#avaliacao
class Insatisfacao(models.Model):
    title = models.CharField(max_length=150,        blank=True,
        null=True)

    def __str__(self):
        return self.title


class Avaliacao(models.Model):
     turista = models.ForeignKey(
        Turista,
        on_delete=models.CASCADE,
        related_name='avaliacoes'
    )
 
     satisfacao_geral_com_a_visita = models.IntegerField()
     insatisfacao_com_a_visita = models.ManyToManyField(Insatisfacao)
     nivel_expectativa = models.IntegerField()
     nivel_satisfacao = models.IntegerField()
     intencao_de_retorno = models.IntegerField()
     precisou_de_algum_servico = models.CharField(max_length=500,        blank=True,
        null=True)
    #de 1 a 10 -> satisfação
    # do que menos gostou ->  satisfação
    # qual era o nivel da expectativa -> percepção
    # quao satisfeito ficou -> satisfação
    #quando pretende voltar -> satisfação
