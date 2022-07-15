from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    
    def __str__(self):
        return self.categoria

class Opcoes(models.Model):
    nome = models.CharField(max_length=200)
    acrecimo = models.FloatField(default=0)