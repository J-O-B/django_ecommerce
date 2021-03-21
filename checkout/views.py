from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Theres nothing in your bag at the moment.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'

    one = "pk_test_51IXYXtIIkFzlANw7WJOV0f7wFCRmVmIqnH"
    two = "9lxcwCRkLdMXIcO68gGlV75QCQXLHdhftMLbhNOvlL"
    three = "gQcdjAiAGHBN003goqSx63"
    full_key = one + two + three
    context = {
        'order_form': order_form,
        'stripe_public_key': full_key,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
