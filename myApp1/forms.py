from django import forms
from myApp1.models import OrderItem


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['item', 'client', 'items_ordered']
        labels = {
            'items_ordered': 'Quantity',
            'client': 'Client Name'
        }
        widgets = {
            'client': forms.RadioSelect()
        }


class InterestForm(forms.Form):
    interested = forms.RadioSelect(choices=(('Yes', 1), ('No', 0)))
    quantity = forms.IntegerField(initial=1, min_value=1)
    comments = forms.Textarea()
