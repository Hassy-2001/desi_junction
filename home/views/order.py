from django.shortcuts import render
from home.models.order import Order
from django.views import View


class Orderview(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'orders.html', {"orders": orders})
