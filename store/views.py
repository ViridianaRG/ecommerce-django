from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.
def store(request, category_slug=None):

    categories = None
    products = None

    if category_slug != None: #Si tiene un slug (la extension de url)
        categories = get_object_or_404(Category, slug=category_slug) #si encuentras la categoria entonces se enlista, de lo contrario lanza una excepcion de tipo 404
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count
    }

    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):

    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug) #el __ sirve para poder obtener el valor del campo de una estructura, en este caso, category
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
    }


    return render(request, 'store/product_details.html', context) #estoy haciendo que tenga el objeto producto en la url
