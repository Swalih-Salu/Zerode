from django.shortcuts import render,redirect
from ProjectApp.models import Product,Details
from .models import Cart,Order
from django.contrib import messages

# Create your views here.

def addCart(req,id):
        
        product=Product.objects.get(id=id)
        user_id=None
        
        try:
            user_id=req.session['user']
        except:
            return redirect('user:login')
   
        try:
            cartitem=Cart.objects.get(product=product)
            if cartitem.quantity<cartitem.product.stock:
                cartitem.quantity +=1
                cartitem.save()
                
            return redirect('cart:display')
                
        except:
            cartitem=Cart(product=product,user_id=user_id,quantity=1)
            cartitem.save()
            return redirect('cart:display')
  
def display(req):
    try:
        user_id = req.session['user']
        # Retrieve all Cart items associated with the user
        cart_items = Cart.objects.filter(user_id=user_id)
        # Calculate total amount
        total_amount = sum(item.product.price * item.quantity for item in cart_items)
        detail=Details.objects.all()
        return render(req, 'cart.html', {"data": cart_items, "total_amount": total_amount,"details":detail})

    except KeyError:
        # If user is not logged in, redirect to login page
        return redirect('user:login')
        
    
       

def Remove(req,id):
    product=Product.objects.get(id=id)
    user_id=req.session["user"]
    
    try:
        cartitem=Cart.objects.get(product=product)
        if  cartitem.quantity>1:
            cartitem.quantity -=1
            cartitem.save()
    except:
        cartitem=Cart(product=product,user_id=user_id,quantity=1)
        cartitem.save()
    return redirect('cart:display')

def Delete(req,id):
     user_id=req.session["user"]
     product=Product.objects.get(id=id)
     category=Cart.objects.get(product=product,user_id=user_id)
     category.delete()
     return redirect('cart:display')
 
def Buy(req):
    cart_items = Cart.objects.all()
    selected_address = req.POST.get('selected_address')
    
    print(type(selected_address))

    for cart_item in cart_items:
        product = cart_item.product
        quantity_to_purchase = cart_item.quantity

        if product.stock >= quantity_to_purchase:
            product.stock -= quantity_to_purchase
            product.save()
            order = Order(quantity=cart_item.quantity, product=cart_item.product, address=selected_address)
            order.save()
            Cart.objects.all().delete()
        else:
            cart_item.delete()

            messages.warning(req, f"Insufficient stock for {product.name}. Item removed from the cart.")

            return redirect('cart:display')
    return redirect('/')



