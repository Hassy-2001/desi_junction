"""
URL configuration for DesiJunction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views.home import Home
from .views.signup import Signup
from .views.login import Login
from .views.login import logout
from .views.order import Orderview
from .views.cart import Cart
from .views.checkout import Checkout
from .middlewares.authentication import auth_middleware

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', Home.as_view(), name="homepage"),
    path('signup.html', Signup.as_view(), name="signup"),
    path('login.html', Login.as_view(), name="login"),
    path('logout.html', logout, name="logout"),
    path('checkout.html', Checkout.as_view(), name="checkout"),
    path('orders.html', auth_middleware(Orderview.as_view()), name="order"),
    path('cart.html', auth_middleware(Cart.as_view()), name="cart"),

]
