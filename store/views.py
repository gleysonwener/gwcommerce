from django.shortcuts import render
from .models import *

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store.html', context)


def cart(request):
    # se o usuário estiver autenticado
    if request.user.is_authenticated:
        customer = request.user.customer # recebe o campo customer de user
        order, created = Order.objects.get_or_create(customer=customer, complete=False) # crinado ou obtendo um pedido
        items = order.orderitem_set.all() # recebendo todos os item do pedido
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'cart.html', context )


def checkout(request):
     # se o usuário estiver autenticado
    if request.user.is_authenticated:
        customer = request.user.customer # recebe o campo customer de user
        order, created = Order.objects.get_or_create(customer=customer, complete=False) # crinado ou obtendo um pedido
        items = order.orderitem_set.all() # recebendo todos os item do pedido
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context )



 