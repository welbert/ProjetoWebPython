from django.db import models
from django.contrib.auth.models import User

class Armamento(models.Model):
    numero_de_serie = models.IntegerField('Numero de Serie',default=0)
    modelo = models.CharField('Modelo',max_length=200)
    fabricante = models.CharField('Fabricante',max_length=200)
    def __str__(self):
        return "Lote: "+str(self.id)+" - "+self.fabricante+"-"+self.modelo


class Municao(models.Model):
    calibre = models.DecimalField('Calibre',max_digits=5, decimal_places=2)
    descricao = models.CharField('Descricao',max_length=250)
    def __str__(self):
        return "Lote: "+str(self.id)+" - "+self.descricao

class Acessorio(models.Model):
    descricao = models.CharField('Descricao',max_length=250)
    def __str__(self):
        return "Lote: "+str(self.id)+" - "+self.descricao

class Reserva_Armamento(models.Model):
    armamento = models.ForeignKey('Armamento')
    reserva = models.ForeignKey('Reserva')
    quantidade = models.FloatField('Quantidade')

class Reserva_Municao(models.Model):
    municao = models.ForeignKey('Municao')
    reserva = models.ForeignKey('Reserva')
    quantidade = models.FloatField('Quantidade')

class Reserva_Acessorio(models.Model):
    acessorio = models.ForeignKey('Acessorio')
    reserva = models.ForeignKey('Reserva')
    quantidade = models.FloatField('Quantidade')

class Reserva(models.Model):
    sigla = models.CharField('Sigla',max_length=5)
    descricao = models.CharField('Descricao',max_length=250)
    def __str__(self):
        return self.sigla

class Cautela_Armamento(models.Model):
    data_de_retirada = models.DateTimeField('Data de Retirada')
    militar = models.ForeignKey('Militar',blank=True,null=True)
    armamento = models.ForeignKey('Armamento')
    quantidade = models.FloatField('Quantidade')
    def __str__(self):
        return str(self.data_de_retirada)

class Cautela_Municao(models.Model):
    data_de_retirada = models.DateTimeField('Data de Retirada')
    militar = models.ForeignKey('Militar',blank=True,null=True)
    municao = models.ForeignKey('Municao')
    quantidade = models.FloatField('Quantidade')
    def __str__(self):
        return str(self.data_de_retirada)

class Cautela_Acessorio(models.Model):
    data_de_retirada = models.DateTimeField('Data de Retirada')
    militar = models.ForeignKey('Militar',blank=True,null=True)
    acessorio = models.ForeignKey('Acessorio')
    quantidade = models.FloatField('Quantidade')
    def __str__(self):
        return str(self.data_de_retirada)

class Militar(models.Model):
    posto = models.CharField('Posto',max_length=60)
    nome_de_guerra = models.CharField('Nome de Guerra',max_length=120)
    reserva = models.ForeignKey('Reserva',blank=True,null=True)
    def __str__(self):
        return "Posto: "+self.posto+" - Nome de Guerra: "+self.nome_de_guerra
