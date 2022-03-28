from django.shortcuts import render, get_object_or_404

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
    return render(request, 'myapp1/placeorder.html', {})
