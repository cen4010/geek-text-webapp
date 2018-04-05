from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from book_details.models import Book
from .models import Cart, CartItem



def cart_home(request):
    print('home')
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    cart_price_update(cart_obj)
    return render(request, "carts/home.html", {"cart": cart_obj})


def cart_checkout(request):
    print('todo')

# used to add books to the from the cart will
#price is hard coded until definition of price is added


def cart_add_book(request):
    price = 10.00
    quantity = request.POST.get('quantity') if request.POST.get(
        'quantity') != None else 1
    book_id = request.POST.get('book_id')
    book_added_price = float(quantity) * price
    print('this is the bookid:' + book_id)
    if book_id is not None:
        add_book = CartItem.objects.create(
            quantity=quantity, book_id=book_id, price=price, book_price_quantity=book_added_price)
        print('this is the add_book:' + str(add_book.id))
        add_book.save()
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        cart_obj.cartItems.add(add_book)
        #updates the session variable for the icon to change on the navbar
        request.session['cart_items'] = cart_obj.cartItems.count()
    return redirect("cart:home")


def cart_remove_book(request):
    cart_item_id = request.POST.get('item_id')
    if cart_item_id is not None:
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        cart_obj.cartItems.remove(cart_item_id)
        #updates the session variable for the icon to change on the navbar
        request.session['cart_items'] = cart_obj.cartItems.count()
    return redirect("cart:home")


def cart_price_update(cart):
    all_cartItems = cart.cartItems.all()
    sub_total = 0
    tax = 1.07
    for x in all_cartItems:
        sub_total += x.price*x.quantity
    cart.subtotal = sub_total
    cart.total = '%.2f' % (tax*float(sub_total))
    cart.save()

