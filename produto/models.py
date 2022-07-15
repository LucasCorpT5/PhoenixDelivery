from django.db import models

# Create your models here.
class teste(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    salario = models.FloatField()