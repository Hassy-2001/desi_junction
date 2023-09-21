from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from home.models.products import Product
from home.models.category import Category
from home.models.customer import Customer
from django.views import View


# DesiJunction homepage code

class Home(View):

    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')

        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print("cart :", request.session['cart'])
        return redirect('homepage')


    def get(self, request):
        cart = request.session.get("cart")
        if not cart:
            request.session['cart']= {}
        products = None
        categories = Category.Get_all_categories()
        categoryid = request.GET.get("category")
        if categoryid:
            products = Product.Get_all_products_by_id(categoryid)
        else:
            products = Product.Get_all_products()

        data = {}
        data['products'] = products
        data['categories'] = categories
        print("you are the same person:", request.session.get('customer'))
        return render(request, 'home.html', data)
