# INF601 - Advanced Programming in Python
# Bunyamin Sari
# Mini Project 4

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login

from .models import Product, CheckOut
from .forms import ProductForm, SignUpForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import transaction, IntegrityError


def home(request):
    return render(request, 'home.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # Retrieve the product from the database
    product = get_object_or_404(Product, pk=product_id)

    # Get checkout information if the product is checked out
    checkout_info = None
    if product.is_checked_out:
        # Assuming you have a related field in the Product model
        checkout = product.checkout_set.first()
        if checkout:
            checkout_info = {
                'user': checkout.checked_out_by.username,
                'timestamp': checkout.checked_out_date,
            }

    return render(request, 'inventory/product_detail.html', {'product': product, 'checkout_info': checkout_info})
    # return render(request, 'inventory/product_detail.html', {'product': product})


@login_required()
def product_edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Check if the logged-in user is the creator of the product
    if product.created_by != request.user:
        messages.error(request, 'You do not have permission to edit this product.')
        return redirect('inventory:product_list')

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('inventory:product_detail', product_id=product.id)  # Redirect to the product detail view
    else:
        form = ProductForm(instance=product)

    return render(request, 'inventory/product_edit.html', {'product': product, 'form': form})


@login_required()
def product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('inventory:product_list')  # Redirect to the product list view after deletion

    return render(request, 'inventory/product_delete.html', {'product': product})


@login_required()
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.created_by = request.user
            new_product.save()
            # After successfully creating a new product
            messages.success(request, 'Product created successfully.')
            return redirect('inventory:product_detail', product_id=new_product.id)
    else:
        form = ProductForm()
    return render(request, 'inventory/product_create.html', {'form': form})


# Create a custom login view that inherits from Django's LoginView
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # You can specify a custom login template
    redirect_authenticated_user = True  # Redirect authenticated users away from the login page


# class CustomLogoutView(LogoutView):
#     template_name = 'registration/logout.html'  # Optional: Provide a custom logout template


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')  # Redirect to the login page upon successful registration
    template_name = 'registration/signup.html'  # Create a registration template


@transaction.atomic
@login_required()
def checkout_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user = request.user  # Get the currently logged-in user

    if product.is_checked_out:
        # If the product is already checked out, display an error message and redirect.
        messages.error(request, 'Product is already checked out.')
        return redirect('inventory:product_list')

    try:
        # Attempt to create a new CheckOut object.
        # If the creation fails (e.g., due to a concurrent request), it will raise an IntegrityError.
        checkout = CheckOut(checked_out_by=user, product=product)
        checkout.save()

        # Lock the product
        product.is_checked_out = True
        product.save()

        # Set a success message
        messages.success(request, 'Product checked out successfully.')

        # Redirect to the product detail page
        return redirect('inventory:product_detail', product_id=product_id)
    except IntegrityError:
        # If an IntegrityError is raised, it means the product was already checked out during this request.
        # Set an error message and redirect.
        messages.error(request, 'Product is already checked out.')
        return redirect('inventory:product_list')


@transaction.atomic
@login_required()
def checkin_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user = request.user  # Get the currently logged-in user

    if not product.is_checked_out:
        # If the product is not checked out, display an error message and redirect.
        messages.error(request, 'Product is not checked out.')
        return redirect('inventory:product_list')

    try:
        # Attempt to find the CheckOut object associated with the product and the user.
        # If found, delete the CheckOut object, effectively checking in the product.
        checkout = CheckOut.objects.get(checked_in_by=user, product=product)
        checkout.delete()

        # Unlock the product
        product.is_checked_out = False
        product.save()

        # Set a success message
        messages.success(request, 'Product checked in successfully.')

        # Redirect to the product detail page
        return redirect('inventory:product_detail', product_id=product_id)
    except CheckOut.DoesNotExist:
        # If the CheckOut object is not found, it means the product is not checked out by the current user.
        # Set an error message and redirect.
        messages.error(request, 'Product is not checked out by you.')
        return redirect('inventory:product_list')

