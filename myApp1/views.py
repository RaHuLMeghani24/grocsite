from django.shortcuts import render, get_object_or_404

from .forms import OrderItemForm, InterestForm
from .models import Type, Item


# Create your views here.
# books=[
#     {
#         'author': 'Usama',
#         'title':'Intro to Django',
#         'date':'March 01, 2022'
#     },
#     {
#         'author': 'Rahul',
#         'title':'Intro to Mental Strength',
#         'date':'March 01, 2022'
#     }
# ]
def index(request):
    # type_list = Type.objects.all().order_by('id')
    type_list = Type.objects.all().order_by('id')[:7]
    return render(request, 'myapp1/index0.html', {'type_list': type_list})


def about(request):
    # return HttpResponse('This is the about page')
    return render(request, 'myApp1/about0.html')


def detail(request, type_no):
    type_with_id = get_object_or_404(Type, pk=type_no)
    # type_with_id = Type.objects.get(id=type_no)
    items_with_type = Item.objects.filter(type=type_with_id)
    context = {
        'type': type_with_id,
        'items': items_with_type
    }
    return render(request, 'myApp1/detail0.html', context)


def items(request):
    itemlist = Item.objects.all().order_by('id')[:20]
    return render(request, 'myapp1/items.html', {'itemlist': itemlist})


def placeorder(request):
    msg = ''
    itemlist = Item.objects.all()
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.items_ordered <= order.item.stock:
                order.save()
                msg = 'Your order has been placed successfully.'
                print('order item', order.item, 'before saving')
                order.item.stock -= order.items_ordered
                order.item.save()
                # TODO remove debug
                print('order item', order.item, 'after saving')
            else:
                msg = 'We do not have sufficient stock to fill your order.'
                return render(request, 'myapp1/order_response.html', {'msg': msg})
    else:
        form = OrderItemForm()
    return render(request, 'myapp1/placeorder.html', {'form': form, 'msg': msg, 'itemlist': itemlist})


def itemdetail(request, item_id):
    form = InterestForm()
    item = Item.objects.get(id=item_id)
    return render(request, 'myApp1/itemdetail.html', {'form': form, 'item': item})
