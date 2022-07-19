from django.shortcuts import render

from produto.models import Categoria

# Create your views here.
def finalizar_pedido(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        erro = request.GET.get('erro')
        total = sum()

def validaCupom(request):
    pass