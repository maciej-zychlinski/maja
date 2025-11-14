from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList
from django.contrib.auth.decorators import login_required

def logout_view(request):
    auth_logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        else:
            return render(request, 'accounts/signup.html', {'form': form})
    form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# @login_required
# def orders_view(request):
#     template_data = {}
#     template_data['title'] = 'Orders'
#     template_data['orders'] = request.user.order_set.all()
#     return render(request, 'accounts/orders.html', {'template_data': template_data})