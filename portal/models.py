from django.db import models
from django.utils import timezone



TIPONEGOCIACAO = (
    ('0', 'Aluguel'),
    ('1', 'Venda'),
)

def sample_upload_to_function(instance, filename):
    extension = filename.split('.')[-1]
    return "imoveis/imovel%s/foto%s.%s" %(instance.id, timezone.now().strftime("%d%m%Y%H%M%S"), extension)

class Imovel(models.Model):
    author = models.ForeignKey('auth.User')
    bairro = models.ForeignKey('Bairro')
    logradouro =  models.TextField()
    quartos = models.IntegerField()
    banheiro = models.IntegerField()
    vagas_garagem = models.IntegerField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    area_construida = models.DecimalField(max_digits=8, decimal_places=2)
    area_total = models.DecimalField(max_digits=8, decimal_places=2)
    tipo = models.ForeignKey('TipoImovel')
    descricao = models.TextField()
    data_inclusao = models.DateTimeField(
        default=timezone.now)
    data_divulgacao = models.DateTimeField(
        blank=True, null=True)
    tipo_negociacao = models.CharField(max_length=1, choices=TIPONEGOCIACAO)

    foto_1 = models.ImageField(upload_to =sample_upload_to_function, null=True, blank=True)
    foto_2 = models.ImageField(upload_to =sample_upload_to_function, null=True, blank=True)
    foto_3 = models.ImageField(upload_to =sample_upload_to_function, null=True, blank=True)
    foto_4 = models.ImageField(upload_to =sample_upload_to_function, null=True, blank=True)
    foto_5 = models.ImageField(upload_to =sample_upload_to_function, null=True, blank=True)
    foto_6 = models.ImageField(upload_to =sample_upload_to_function, null=True, blank=True)
    foto_7 = models.ImageField(upload_to =sample_upload_to_function, null=True, blank=True)
    foto_8 = models.ImageField(upload_to =sample_upload_to_function, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Imoveis"

    def divulgacao(self):
        self.data_divulgacao = timezone.now()
        self.save()

    def __str__(self):
        return self.tipo.descricao+" - "+self.bairro.descricao+" - "+self.logradouro


class TipoImovel(models.Model):
    author = models.ForeignKey('auth.User')
    descricao = models.TextField()
    data_inclusao = models.DateTimeField(
        default=timezone.now)

    class Meta:
        verbose_name_plural = "Tipo Imoveis"

    def __str__(self):
        return self.descricao


class Cidade(models.Model):
    author = models.ForeignKey('auth.User')
    descricao = models.TextField()
    data_inclusao = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.descricao


class Bairro(models.Model):
    author = models.ForeignKey('auth.User')
    descricao = models.TextField()
    cidade = models.ForeignKey('Cidade')
    data_inclusao = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.descricao