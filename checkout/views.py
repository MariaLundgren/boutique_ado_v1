from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag: 
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('procucts'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JC2e4D4TazcLgOwNy1qqr9sVnpPZ4wN9R9ZM4l4grzTKa8wpCa4z3zM4o9V16rwpQu2T9jg8uQ0DE7E05okVD1O00a3HHhGJ3',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
