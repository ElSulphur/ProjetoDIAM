from django.db import models
import datetime
# Create your models here.

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=1000)
    local = models.CharField(max_length=500)
    data = models.DateTimeField('data evento')
    def __str__(self):
        return self.nome

