from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


TIPONEGOCIACAO = (
    ('0', 'Aluguel'),
    ('1', 'Venda'),
)


class Destaque(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, editable=False)
    imovel = models.ForeignKey('Imovel')
    data_inicio_divulgacao = models.DateTimeField(
        blank=True, null=True)
    data_final_divulgacao = models.DateTimeField(
        blank=True, null=True)

    def __str__(self):
        return self.imovel.__str__()




def sample_upload_to_function(instance, filename):
    extension = filename.split('.')[-1]
    return "imoveis/imovel%s/foto%s.%s" %(instance.id, timezone.now().strftime("%d%m%Y%H%M%S"), extension)

class Imovel(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, editable=False)
    proprietario = models.ForeignKey('Proprietario')
    bairro = models.ForeignKey('Bairro')
    logradouro =  models.TextField()
    quartos = models.IntegerField(blank=True, null=True)
    banheiro = models.IntegerField(blank=True, null=True)
    vagas_garagem = models.IntegerField(blank=True, null=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    area_construida = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2)
    area_total = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2)
    tipo = models.ForeignKey('TipoImovel')
    descricao = models.TextField()
    data_inclusao = models.DateTimeField(default=timezone.now)
    data_divulgacao = models.DateTimeField(default=timezone.now)
    tipo_negociacao = models.CharField(max_length=1, choices=TIPONEGOCIACAO)

    foto_1 = models.ImageField(upload_to =sample_upload_to_function)
    foto_2 = models.ImageField(upload_to =sample_upload_to_function, null=True, blank=True)
    foto_3 = models.ImageField(upload_to =sample_upload_to_function, null=True, blank=True)
    foto_4 = models.ImageField(upload_to =sample_upload_to_function, null=True, blank=True)
    foto_5 = models.ImageField(upload_to =sample_upload_to_function, null=True, blank=True)
    foto_6 = models.ImageField(upload_to =sample_upload_to_function, null=True, blank=True)
    foto_7 = models.ImageField(upload_to =sample_upload_to_function, null=True, blank=True)
    foto_8 = models.ImageField(upload_to =sample_upload_to_function, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Imoveis"

    def __str__(self):
        return "Ref: "+str(self.id)+" - "+self.tipo.descricao+" - "+self.get_tipo_negociacao()+" - "+self.bairro.descricao+" - "+self.bairro.cidade.descricao+" - "+self.logradouro

    def get_tipo_negociacao(self):
        return self.get_tipo_negociacao_display()

    get_tipo_negociacao.short_description = 'Tipo Negociacao'


class TipoImovel(models.Model):
    descricao = models.TextField()
    data_inclusao = models.DateTimeField(
        default=timezone.now)

    class Meta:
        verbose_name_plural = "Tipo Imoveis"

    def __str__(self):
        return self.descricao


class Cidade(models.Model):
    descricao = models.TextField()
    data_inclusao = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.descricao


class Bairro(models.Model):
    descricao = models.TextField()
    cidade = models.ForeignKey('Cidade')
    data_inclusao = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.descricao+" - "+self.cidade.descricao

class Proprietario(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, editable=False)
    nome = models.CharField( max_length=255 )
    cpf = models.CharField( max_length=14 )
    rg = models.CharField( max_length=12 )
    telefone_fixo = models.CharField( max_length=13, null=True, blank=True)
    celular_1 = models.CharField( max_length=13, null=True, blank=True)
    celular_2 = models.CharField( max_length=13, null=True, blank=True)
    email = models.CharField( max_length=255, null=True, blank=True)
    telefone_comercial = models.CharField( max_length=13, null=True, blank=True)

    def __str__(self):
        return "CPF: "+self.cpf+" - Nome: "+self.nome