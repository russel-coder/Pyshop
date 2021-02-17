
from django.shortcuts import render

from .models import Product, New


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    new = New.objects.all()
    return render(request, 'new.html', {'new': new})
