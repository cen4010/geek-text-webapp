from django.shortcuts import render, redirect
from .models import Cart
from .models import CartItem

#render cart home
def cart_home(request):
    cart_obj = Cart.objects.new_or_get(request)
    return render(request, "home.html", {"cart": cart_obj})

# used to add books to the from the cart will
#price is hard coded until definition of price is added
def cart_add_book(request):
    price=10.00
    quantity = request.POST.get('quantity') if request.POST.get(
        'quantity') != None else 1
    book_id = request.POST.get('bookId')
    book_added_price = float(quantity) * price

    if book_id is not None:
        add_book = CartItem.objects.create(quantity=quantity, book_id=book_id, price=price,book_price_quantity=book_added_price)
        add_book.save()
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        cart_obj.cartitems.add(add_book)
        #updates the session variable for the icon to change on the navbar
        request.session['cart_items'] = cart_obj.cartitems.count()
    return redirect("cart:home")


