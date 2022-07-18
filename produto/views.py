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
        
        # descompactando os adicionais
        for i, j in adicionais:
            for k in j:
                preco_total += Opcoes.objects.filter(id=int(k))[0].acrecimo # filtrando o total do acrecimo + o produto
    
    def troca_id_por_nome_adicional(adicional):
        adicionais_com_nomes = []
        for i in adicionais:
            opcoes = []
            for j in i[1]:
                op = Opcoes.objects.filter(id = int(j))[0].nome
                opcoes.append(op)
            adicionais_com_nomes.append((i[0], opcoes))
        return adicionais_com_nomes

    adicionais = troca_id_por_nome_adicional(adicionais)

    preco_total *= int(x['quantidade'][0])

    data = {'id_produto': int(x['id'][0]),
            'observacoes': x['observacoes'][0],
            'preco': preco_total,
            'adicionais': adicionais,
            'quantidade': x['quantidade'][0]
            }

    request.session['carrinho'].append(data)
    request.session.save()
    
    return redirect(f'/ver_carrinho')

def ver_carrinho(request):
    categorias = Categoria.objects.all()
    dados_mostrar = []
    for i in request.session['carrinho']:
        prod = Produto.objects.filter(id=i['id_produto'])
        