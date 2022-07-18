from django.db import models

# Create your models here.
class Pedido(models.Model):
    usuario = models.CharField(max_length=200)