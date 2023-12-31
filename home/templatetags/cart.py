from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()
    for id in keys:
        try:
            a = int(id)
        except:
            if a == product.id:
                return True
    return False


@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0


@register.filter(name='total_price')
def total_price(product, cart):
    return product.product_price * cart_quantity(product, cart)


@register.filter(name='total_product_price')
def total_product_price(products, cart):
    sum = 0;
    for p in products:
        sum += total_price(p, cart)
    return sum;
