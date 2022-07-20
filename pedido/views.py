from django.shortcuts import render
from pedido.models import Pedido, CupomDesconto, ItemPedido
from produto.models import Categoria, Produto

# Create your views here.
def finalizar_pedido(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        erro = request.GET.get('erro')
        total = sum([float(i['preco']) for i in request.session['carrinho']])
        return render(request, 'finalizar_pedido.html', {
                    'carrinho': len(request.session['carrinho']),
                    'categorias': categorias,
                    'total': total,
                    'erro': erro
                    })
    else:
        if len(request.session['carrinho']) > 0:
            x = request.POST
            total = sum([float(i['preco']) for i in request.session['carrinho']])
            cupom = CupomDesconto.objects.filter(codigo=x['cupom'])
            cupom_salvar = None
            if len(cupom) > 0 and cupom[0].ativo:
                total = total - ((total*cupom[0].desconto)/100)
                cupom[0].usos += 1
                cupom[0].save()
                cupom_salvar = cupom[0]

            carrinho = request.session.get('carrinho')
            listaCarrinho = []
            for i in carrinho:
                listaCarrinho.append({
                    'produto': Produto.objects.filter(id=i['id_produto'])[0],
                    'observacoes': i['observacoes'],
                    
                })
def validaCupom(request):
    pass