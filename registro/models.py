from django.db import models


class Armamento(models.Model):
    numero_de_serie = models.IntegerField(default=0)
    modelo = models.CharField(max_length=200)
    fabricante = models.CharField(max_length=200)
    def __str__(self):
        return "Numero de Serie: "+str(self.numero_de_serie)+" - Modelo: "+self.modelo+" - Fabricante: "+self.fabricante

class Reserva(models.Model):
    sigla = models.CharField(max_length=5)
    descricao = models.CharField(max_length=250)
    def __str__(self):
        return "Sigla: "+self.sigla+" - Descricao: "+self.descricao

class Municao(models.Model):
    calibre = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.CharField(max_length=250)
    def __str__(self):
        return "Calibre: "+str(self.calibre)+" - Descricao: "+self.descricao

class Acessorio(models.Model):
    descricao = models.CharField(max_length=250)
    def __str__(self):
        return "Descricao: "+self.descricao

class Militar(models.Model):
    posto = models.CharField(max_length=60)
    nome_de_guerra = models.CharField(max_length=120)
    def __str__(self):
        return "Posto: "+self.posto+" - Nome de Guerra: "+self.nome_de_guerra
