from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from home.models.products import Product
from home.models.category import Category
from home.models.customer import Customer
from django.views import View


# customer signup code

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        error_message = None

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'phone': phone
        }

        customer = Customer(first_name=first_name, last_name=last_name,
                            email=email, phone=phone, password=password)

        if not (customer.first_name):
            error_message = "First name is required !!"
        elif len(customer.first_name) < 4:
            error_message = "First name must be 4 character long or more !!"
        elif not customer.last_name:
            error_message = "Last name is required !!"
        elif len(customer.last_name) < 4:
            error_message = "Last name must be 4 character long or more !!"
        elif not customer.phone:
            error_message = "Phone number is required !!"
        elif len(customer.phone) < 11:
            error_message = "Phone number must be 11 character long !!"
        elif not customer.password:
            error_message = "Password is required !!"
        elif len(customer.password) < 8:
            error_message = "Password must be 8 character long or more !!"
        elif not customer.email:
            error_message = "Email is required !!"
        elif len(customer.email) < 6:
            error_message = "Email must be 6 character long or more !!"
        elif customer.isExists():
            error_message = "Email address already registered !!"
            return error_message

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)
