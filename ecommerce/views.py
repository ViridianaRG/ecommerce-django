from django.shortcuts import render
from store.models import Product

def home(request):

    products = Product.objects.all().filter(is_available = True) #Traer todos los productos que estan activos

    context = {
        'products': products,
    }

    return render(request, 'home.html', context)