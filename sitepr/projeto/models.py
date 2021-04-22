from django.contrib.auth.models import User
from django.db import models
import datetime
# Create your models here.




class Organizacao(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, )
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=1000)
    avatar = models.ImageField()
    is_organizacao = models.BooleanField(default=True)
    def __str__(self):
       return self.nome


class Evento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=1000)
    local = models.CharField(max_length=500)
    data = models.DateTimeField('data evento')
    organizacao = models.ForeignKey(Organizacao, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome



