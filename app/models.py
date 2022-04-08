from django.db import models

# Create your models here.
class Clientes(models.Model):
    Nome = models.CharField(max_length=150)
    Cpf = models.IntegerField()
    DataNascimento = models.IntegerField()