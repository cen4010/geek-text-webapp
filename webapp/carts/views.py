from django.http import HttpResponse
from django.shortcuts import render, redirect

def cart_page(request):

    return render(request, "cart/cart.html")