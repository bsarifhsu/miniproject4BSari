from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

from .forms import ProductForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'inventory/product_detail.html', {'product': product})


def product_edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('inventory:product_detail', product_id=product.id)  # Redirect to the product detail view
    else:
        form = ProductForm(instance=product)

    return render(request, 'inventory/product_edit.html', {'product': product, 'form': form})


def product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('inventory:product_list')  # Redirect to the product list view after deletion

    return render(request, 'inventory/product_delete.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            new_product = form.save()
            return redirect('inventory:product_detail', product_id=new_product.id)
    else:
        form = ProductForm()

    return render(request, 'inventory/product_create.html', {'form': form})



