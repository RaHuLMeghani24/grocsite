from django.contrib import admin
from django.db import models

from .models import Type, Item, Client, OrderItem


def firstnameupper(obj):
    return obj.first_name.upper()


@admin.action(description='change the city name to Chatam')
def change_city(modeladmin, request, queryset: models.QuerySet):
    queryset.update(city='CH')


class ClientAdmin(admin.ModelAdmin):
    # can include things possible in existing model
    list_display = ('first_name', 'city')
    ordering = ['first_name']
    fields = [('first_name', 'last_name'), 'city']
    actions = [change_city]


# or you can use StackedInline
class ItemInline(admin.TabularInline):
    model = Item


class TypeAdmin(admin.ModelAdmin):
    inlines = [ItemInline]


# Register your models here.
admin.site.register(Type, TypeAdmin)
admin.site.register(Item)
admin.site.register(Client, ClientAdmin)
admin.site.register(OrderItem)
