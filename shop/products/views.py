from django.shortcuts import redirect, render
from .models import Product, Cart
from django.views import generic
from django.contrib.auth.models import User
from django.db.models import Sum


# Create your views here.
class ShowProducts(generic.ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'


class AboutProduct(generic.DetailView):
    model = Product
    template_name = 'products/about.html'
    context_object_name = 'product'


class CartDetail(generic.ListView):
    model = Cart
    template_name = 'products/cart.html'
    context_object_name = 'orders'


class Signup(generic.ListView):
    model = Product
    template_name = 'products/signup.html'


def addToCart(request, pk):
    product = Product.objects.get(id=pk)
    try:
        order = Cart.objects.get(user=request.user, product=product)
        order.quantity += 1
        order.save()
    except:
        order = Cart.objects.create(product=product, user=User.objects.get(id = request.user.id))
        order.save()
    return redirect('home')


# def total_price(request):
#     total_sum = Product.objects.filter(user=request.user).aggregate(sum=Sum('price'))
#     return render(request, 'products/checkout.html', {'total_sum': total_sum})
