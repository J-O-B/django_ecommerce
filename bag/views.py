from django.shortcuts import (render, redirect,
                              reverse, HttpResponse,
                              get_object_or_404)
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """
    A view of a users shopping bag
    """
    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """
    Add a quantity of the specified product to the shopping bag
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                mess = f'Updated size {size.upper()} {product.name}.'
                mess2 = f' You now have {bag[item_id]["items_by_size"][size]}'
                mess3 = ' of this product in your shopping bag.'
                messages.success(request, mess + mess2 + mess3)
            else:
                bag[item_id]['items_by_size'][size] = quantity
                mess = f'Added {size.upper()}'
                mess1 = f' {product.name} to your bag.'
                messages.success(request, mess + mess1)

        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            mess = f'Added {size.upper()}'
            mess1 = f' {product.name} to your bag.'
            messages.success(request, mess + mess1)

    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            mess = f'You now have {bag[item_id]}'
            mess1 = f' {product.name}s in your shopping bag.'
            messages.success(request, mess + mess1)

        else:
            bag[item_id] = quantity
            mess = f'Added {bag[item_id]} {product.name} to your bag.'
            messages.success(request, mess)

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust bag items in bag
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            mess = f'Updated {size.upper()} sized {product.name}.'
            mess2 = f' You now have {bag[item_id]["items_by_size"][size]}'
            mess3 = ' of this product in your shopping bag.'
            messages.success(request, mess + mess2 + mess3)
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size'][size]:
                bag.pop(item_id)
            mess = f'Removed {size.upper()} {product.name} from your bag.'
            messages.success(request, mess)
    else:
        if quantity > 0:
            bag[item_id] = quantity
            mess = f'You now have {bag[item_id]}'
            mess1 = f' {product.name}s in your shopping bag.'
            messages.success(request, mess + mess1)

        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag.')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            mess = f'Removed {size.upper()} {product.name} from your bag'
            messages.success(request, mess)
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag.')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item {e}')
        return HttpResponse(status=500)
