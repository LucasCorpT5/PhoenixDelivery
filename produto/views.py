from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    if not request.session.get("carrinho"):
        request.session['carrinho'] = []
        request.session.save()
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    # print(produtos[0].img)s
    return render(request, 'home.html', {'produtos': produtos, 
    'carrinho': len(request.session['carrinho']), 'categorias': categorias})

def categoria(request, id): # o id veio atravez da url
    produtos = Produto.objects.filter(categoria_id = id)
    categorias = Categoria.objects.all()