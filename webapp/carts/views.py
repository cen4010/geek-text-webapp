from django.shortcuts import render, redirect
from django.contrib import messages
from book_details.models import Book
from .models import Cart, CartItem, OrderItem, Order, SavedItems


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    saved_obj = SavedItems.objects.all()
    cart_price_update(cart_obj)
    return render(request, "carts/home.html", {"cart": cart_obj, "Saveditems": saved_obj})


def cart_checkout_home(request):
     return render(request, "carts/checkout.html")


def cart_checkout(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    all_cartItems = cart_obj.cartItems.all()
    order = Order.objects.create()

    for item in all_cartItems:
        line_item = item.price*item.quantity
        add_order_item = OrderItem.objects.create(
            quantity=item.quantity, book_id=item.book.id,
            price=item.price, book_price_quantity=line_item
        )
        add_order_item.save()
        order.orderItems.add(add_order_item)
        cart_obj.cartItems.remove(item)

    order.subtotal = cart_obj.subtotal
    order.total = cart_obj.total
    order.user = cart_obj.user
    order.save()

    return redirect("cart:checkout_home")


def cart_add_book(request):
    quantity = request.POST.get('quantity') if request.POST.get(
        'quantity') != None else 1
    book_id = request.POST.get('book_id')
    print('this is the bookid:' + book_id)
    if book_id is not None:
        book = Book.objects.get(id=book_id)
        price = float(book.price.amount)
        add_book = CartItem.objects.create(
            quantity=quantity, book_id=book_id, price=price)

        add_book.save()
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        cart_obj.cartItems.add(add_book)
    return redirect("cart:home")


def cart_update_quantity(request):
    quantity = request.POST.get('quantity') if request.POST.get(
        'quantity') != None else 1
    item_id = request.POST.get('cartItemId')
    item = CartItem.objects.get(id=item_id)
    item.quantity = quantity
    item.save()

    return redirect("cart:home")


def cart_save_for_later(request):
    cart_item_id = request.POST.get('item_id')
    if cart_item_id is not None:
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        item = CartItem.objects.get(id=cart_item_id)
        saved_book = SavedItems()
        saved_book.book = item.book
        cart_obj.cartItems.remove(cart_item_id)
        saved_book.save()
    return redirect('cart:home')


def cart_delete_from_saved(request):
    savedItems_id = request.POST.get('item_id')
    saved_book = SavedItems.objects.get(id=savedItems_id)
    saved_book.delete()
    return redirect('cart:home')


def cart_add_back(request):
    savedItems_id = request.POST.get('item_id')
    print(savedItems_id)
    saved_book = SavedItems.objects.get(id=savedItems_id)
    book_id = saved_book.book.id
    book_id = str(book_id)
    if book_id is not None:
        book = Book.objects.get(id=book_id)
        price = float(book.price.amount)
        add_book = CartItem.objects.create(
            quantity=1, book_id=book_id, price=price)

        add_book.save()
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        cart_obj.cartItems.add(add_book)
        saved_book.delete()
    return redirect('cart:home')


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
