from django import template

register = template.Library()

@register.filter(name='Currency_sign')
def Currency_sign(number):
    return "₨. " + str(number)

@register.filter(name='multiply')
def multiply(number1,number2):
    return number1 * number2