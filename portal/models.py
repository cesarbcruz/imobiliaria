from django.db import models
from django.utils import timezone

class Imovel(models.Model):
    author = models.ForeignKey('auth.User')
    bairro = models.ForeignKey('Bairro')
    quartos = models.IntegerField()
    banheiro = models.IntegerField()
    vagasGaragem = models.IntegerField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    areaConstruida = models.DecimalField(max_digits=8, decimal_places=2)
    areaTotal = models.DecimalField(max_digits=8, decimal_places=2)
    tipo = models.ForeignKey('TipoImovel')
    descricao = models.TextField()
    data_inclusao = models.DateTimeField(
            default=timezone.now)
    data_divulgacao = models.DateTimeField(
            blank=True, null=True)

    def divulgacao(self):
        self.data_divulgacao = timezone.now()
        self.save()

    def __str__(self):
        return self.tipo.descricao


class TipoImovel(models.Model):
    author = models.ForeignKey('auth.User')
    descricao = models.TextField()
    data_inclusao = models.DateTimeField(
            default=timezone.now)

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