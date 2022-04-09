from django.db import models

# Create your models here.
class Atleta(models.Model):
    Nome = models.CharField(max_length=150)
    Idade = models.IntegerField()
    Selecao = models.CharField(max_length=150)