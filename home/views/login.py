from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from home.models.customer import Customer
from django.views import View


# customer login code

class Login(View):
    return_Url = None
    def get(self, request):
        Login.return_Url = request.GET.get("return_Url")
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.Get_customer_by_email(email)
        error_message = None

        values = {
            "email": email
        }

        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_Url:
                    return HttpResponseRedirect(Login.return_Url)
                else:
                    Login.return_Url = None
                    return redirect('homepage')
            else:
                error_message = "Email or Password is Invalid !!"
        else:
            error_message = "Email or Password is Invalid !!"

        dataset = {
            'error': error_message,
            'values': values
        }
        return render(request, 'login.html', dataset)


def logout(request):
    request.session.clear()
    return redirect("login")
