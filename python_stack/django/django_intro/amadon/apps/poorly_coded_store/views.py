from django.shortcuts import render, redirect
from .models import Order, Product


def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)


def process_order(request):

    # Process the order here. We don't want to process
    # in the same method that we render the checkout page.

    # Calculate the order amounts here
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    print('total_charge', total_charge)

    # Print to the terminal and create the order record
    print("Charging credit card...")

    # TODO: Add a try/catch for this order creation
    Order.objects.create(
        quantity_ordered=quantity_from_form, total_price=total_charge)

    # Store current order info
    request.session['quantity_from_form'] = quantity_from_form
    request.session['price_from_form'] = price_from_form
    request.session['total_charge'] = total_charge

    # Keep running total of ordered and spent
    request.session['total_ordered'] += quantity_from_form
    request.session['total_spent'] += total_charge

    # Call the checkout method, which will render the checkout page.
    return redirect("/checkout")


def checkout(request):

    return render(request, "store/checkout.html")
