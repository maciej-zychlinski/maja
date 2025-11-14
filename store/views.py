from django.shortcuts import render, get_object_or_404
from .models import Product, Review, Category
from cart.forms import CartAddProductForm

def product_list(request):
    search_term = request.GET.get('search')
    if search_term:
        products = Product.objects.filter(name__icontains=search_term)
    else:
        products = Product.objects.all()
    
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'store/product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(product=product)
    cart_product_form = CartAddProductForm()
    
    context = {
        'product': product,
        'reviews': reviews,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'store/product_detail.html', context)