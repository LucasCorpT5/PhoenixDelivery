from django.shortcuts import render
from pedido.models import Pedido, CupomDesconto, ItemPedido
from produto.models import Categoria

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

def validaCupom(request):
    pass