from distutils.command.upload import upload
from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    
    def __str__(self):
        return self.categoria

class Opcoes(models.Model):
    nome = models.CharField(max_length=200)
    acrecimo = models.FloatField(default=0)

    def __str__(self):
        return self.nome

class Adicional(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    maximo = models.IntegerField()
    minimo = models.IntegerField()
    opcoes = models.ManyToManyField(Opcoes)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome_produto = models.CharField(max_length=200)
    img = models.ImageField(upload_to='post_img')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.FloatField()
    descricao = models.TextField() # sem limite de caracteres
    ingredientes = models.CharField(max_length=2000)
    adicionais = models.ManyToManyField(Adicional, blank=True)
    ativo = models.BooleanField(default=True)

    @mark_safe
    def icone(self):
        return f'<img width="30px" src="/media/{self.img}"> '

    def __str__(self):
        return self.nome_produto