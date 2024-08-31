from django.shortcuts import render, redirect
from .models import Cart
from store.models import Product



def cart_detail(request):
    return render(request, 'carts/cart_detail.html')


def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():  # если у пользователя уже добавлен этот товар в корзину
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else: # если такого товара нет то создаем корзину с таким товаром
            Cart.objects.create(user=request.user, product=product, quantity=1)

    return redirect('cart:cart_detail')

def cart_change(request):
    cart_id = request.POST.get('cart_id')
    quantity = request.POST.get('quantity')

    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()

    return redirect(request.META['HTTP_REFERER'])


def cart_remove(request, product_id):
    cart = Cart.objects.get(id=product_id)
    cart.delete()

    # в параметре request атрибута META обращаемся по ключу, он отвечает с какой страницы мы сюда попали
    return redirect(request.META['HTTP_REFERER'])
