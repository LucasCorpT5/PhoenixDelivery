from django.contrib import admin
from .models import Pedido, ItemPedido

# Register your models here.
class itemPedidoInline(admin.TabularInline):
    readonly_fields = ('produto', 'quantidade', 'preco', 'descricao', 'adicionais',)
    model = ItemPedido
    extra = 1