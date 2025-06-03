from django.db import models

# Create your models here.

#Turista
class Turista(models.Model):

    class FaixaEtaria(models.IntegerChoices):
        DE_18_A_24 = 0, '18 a 24 anos'
        DE_25_A_34 = 1, '25 a 34 anos'
        DE_35_A_44 = 2, '35 a 44 anos'
        DE_45_A_54 = 3, '45 a 54 anos'
        DE_55_A_64 = 4, '55 a 64 anos'
        MAIS_DE_65 = 5, '65 anos ou mais'

    class Pais(models.TextChoices):
        BRASIL    = 'br', 'Brasil'
        ARGENTINA = 'ar', 'Argentina'
        ALEMANHA  = 'de', 'Germany'
        FRANCA    = 'fr', 'France'

    class Estado(models.TextChoices):
        SP = 'SP', 'São Paulo'
        RJ = 'RJ', 'Rio de Janeiro'
        MG = 'MG', 'Minas Gerais'
        RS = 'RS', 'Rio Grande do Sul'
	
    class Cidade(models.TextChoices): 
        SP ='sao_paulo', 'São Paulo'
        RJ = 'rio', 'Rio de Janeiro'
        BELO_HORIZONTE = 'bh', 'Belo Horizonte'
        PORTO_ALEGRE='poa', 'Porto Alegre'

    class Genero(models.TextChoices):
        HOMEM = 'male','Masculino'
        MULHER = 'female','Feminino'
        NAO_BINARIO = 'non_binary','Não binário'
        OUTRO = 'other','Outro'
        OMITIR = 'omit','Prefiro nao informar'

    class Escolaridade(models.IntegerChoices):
        FUNDAMENTAL_INCOMPLETO    = 0, 'Ensino fundamental incompleto'
        FUNDAMENTAL_COMPLETO      = 1, 'Ensino fundamental completo'
        MEDIO_INCOMPLETO          = 2, 'Ensino médio incompleto'
        MEDIO_COMPLETO            = 3, 'Ensino médio completo'
        SUPERIOR_INCOMPLETO       = 4, 'Ensino superior incompleto'
        SUPERIOR_COMPLETO         = 5, 'Ensino superior completo'

    class RendaEstimada(models.TextChoices):
        LOW        = 'low',      'Menos de R$1.000'
        LOW_MID    = 'low_mid',  'R$1.000 - R$3.000'
        MID        = 'mid',      'R$3.000 - R$5.000'
        HIGH_MID   = 'high_mid', 'R$5.000 - R$10.000'
        HIGH       = 'high',     'Mais de R$10.000'
        OMIT       = 'omit',     'Prefiro não informar'


    pais = models.CharField(max_length=2,
     choices=Pais.choices,
     verbose_name='país do turista') 

    estado = models.CharField(max_length=50,
    choices=Estado.choices,
    verbose_name='estado')
    
    cidade = models.CharField(max_length=50,
    choices=Cidade.choices,
    verbose_name='cidade')

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
    title = models.CharField(max_length=150)


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
 


    class TempoEstadia(models.IntegerChoices):
        UM_DIA = 0, '1 dia'
        DOIS_TRES_DIAS = 1, '2 a 3 dias'
        FIM_DE_SEMANA = 2, 'Apenas no final de semana'
        QUATRO_DIAS = 3, '4 dias'
        CINCO_DIAS = 4, '5 dias'
        UMA_SEMANA = 5, '1 semana'
        QUINZE_DIAS = 6, '15 dias'
        MAIS_QUINZE = 7, 'Mais de 15 dias'

    class Reincidencia(models.IntegerChoices):
        DUAS_A_CINCO = 0, 'Já visitei entre 2 e 5 vezes'
        CINCO_A_DEZ = 1, 'Já visitei entre 5 e 10 vezes'
        MAIS_DE_DEZ = 2, 'Já visitei mais de 10 vezes'
        MENSAL = 3, 'Visito uma vez por mês'
        FIM_DE_SEMANA_FREQ = 4, 'Visito a cada fim de semana'



    class GastoDiario(models.IntegerChoices):
        ATE_300 = 0, 'Até R$ 300,00'
        DE_300_A_500 = 1, 'De R$ 300,00 a R$ 500,00'
        DE_500_A_1000 = 2, 'De R$ 500,00 a R$ 1.000,00'
        DE_1000_A_1500 = 3, 'De R$ 1.000,00 a R$ 1.500,00'
        DE_1500_A_2000 = 4, 'De R$ 1.500,00 a R$ 2.000,00'
        DE_2000_A_3000 = 5, 'De R$ 2.000,00 a R$ 3.000,00'
        DE_3000_A_5000 = 6, 'De R$ 3.000,00 a R$ 5.000,00'
        MAIS_5000 = 7, 'Acima de R$ 5.000,00'

    ja_visitou = models.BooleanField(default=False)
    conhece_a_rota_mirantes = models.BooleanField(default=False)
    motivo = models.ManyToManyField(Motivo)
    veiculo_utilizado = models.ManyToManyField(Veiculo)
    tempo_de_estadia = models.IntegerField(choices=TempoEstadia.choices)
    reincidencia = models.IntegerField(choices=Reincidencia.choices)
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
    title = models.CharField(max_length=150)


    def __str__(self):
        return self.title

class AtividadesRealizadas(models.Model):

    locais_visitados = models.ManyToManyField(LocaisVisitados)
    participacao_em_eventos = models.ManyToManyField(ParticipacaoEmEventos)
    aplicativos = models.ManyToManyField(AplicativosUtilizados)




#planejamento
class FonteInformacao(models.Model):
    title = models.CharField(max_length=30)


    def __str__(self):
        return self.title

class Planejamento(models.Model):

    class Antecedencia(models.IntegerChoices):
        MENOS_DE_1_MES  = 0, 'Menos de 1 mês'
        UM_A_3_MESES    = 1, '1 a 3 meses'
        TRES_A_6_MESES  = 2, '3 a 6 meses'
        MAIS_DE_6_MESES = 3, 'Mais de 6 meses'


    class Organizacao(models.IntegerChoices):

        VIAGEM_INDIVIDUAL   = 0, 'Viagem individual'
        VIAGEM_EM_CASAL = 1, 'Viagem em casal'
        VIAGEM_EM_FAMILIA   = 2, 'Viagem em família'
        VIAGEM_EM_GRUPO = 3, 'Viagem em grupo'
        COM_AGENCIA_DE_VIAGENS  = 4, 'Com agência de viagens'
        OUTRO   = 5, 'Outro'


    viagem_planejada = models.BooleanField(default=False)
    antecedencia_do_planejamento = models.IntegerField(
        choices=Antecedencia.choices,
        verbose_name='antecedência do planejamento'
    )
    
    fontes_de_informacao_utilizadas = models.ManyToManyField(FonteInformacao)

    forma_de_organizacao = models.IntegerField(
        choices=Organizacao.choices,
        verbose_name='forma de organização'
    )



#avaliacao
class Insatisfacao(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Avaliacao(models.Model):
     satisfacao_geral_com_a_visita = models.IntegerField()
     insatisfacao_com_a_visita = models.ManyToManyField(Insatisfacao)
     nivel_expectativa = models.IntegerField()
     nivel_satisfacao = models.IntegerField()
     intencao_de_retorno = models.IntegerField()
     precisou_de_algum_servico = models.CharField(max_length=255)
    #de 1 a 10 -> satisfação
    # do que menos gostou ->  satisfação
    # qual era o nivel da expectativa -> percepção
    # quao satisfeito ficou -> satisfação
    #quando pretende voltar -> satisfação
