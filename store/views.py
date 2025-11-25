from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Review, Category
from .forms import ReviewForm
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
    review_form = ReviewForm()
    
    context = {
        'product': product,
        'reviews': reviews,
        'cart_product_form': cart_product_form,
        'review_form': review_form,
    }
    return render(request, 'store/product_detail.html', context)

@login_required
def add_review(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('store:product_detail', pk=product.pk)
    return redirect('store:product_detail', pk=product.pk)