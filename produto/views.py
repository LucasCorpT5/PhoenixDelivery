from django.shortcuts import redirect, render
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

def categorias(request, id): # o id veio atravez da url
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    produtos = Produto.objects.filter(categoria_id = id)
    categorias = Categoria.objects.all()

    return render(request, 'home.html', {'produtos': produtos,
                                        'carrinho': len(request.session['carrinho']),
                                        'categorias': categorias})

def produto(request, id):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    erro = request.GET.get('erro')
    produto = Produto.objects.filter(id=id)[0]
    categorias = Categoria.objects.all()
    return render(request, 'produto.html', {'produto': produto, 
                                            'carrinho': len(request.session['carrinho']),
                                            'categorias': categorias,
                                            'erro': erro})

def add_carrinho(request):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()

    x = dict(request.POST)
    def removeLixo():
        adicionais = x.copy() # o copy cria outra referencia de lista
        adicionais.pop('id')
        adicionais.pop('csrfmiddlewaretoken')
        adicionais.pop('observacoes')
        adicionais.pop('quantidade')
        adicionais = list(adicionais.items())

        return adicionais
    
    adicionais = removeLixo()
    id = int(x['id'][0])
    preco_total = Produto.objects.filter(id=id)[0].preco # pegando o preco de um produto
    adicionais_verifica = Adicional.objects.filter(produto = id)
    aprovado = True

    for i in adicionais_verifica:
        encontrou = False
        minimo = i.minimo
        maximo = i.maximo
        for j in adicionais:
            if i.nome == j[0]:
                encontrou = True
                if len(j[1]) < minimo or len(j[1]) > maximo:
                    aprovado = False
        if minimo > 0 and encontrou == False:
            aprovado = False
        
        if not aprovado:
            return redirect(f'/produto/{id}?erro=1')
        
        for i, j in adicionais:
            for k in j:
                pass