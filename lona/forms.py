from django import forms
from .models import Customer, Item, Loan, Payment


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address', 'id_number']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'serial_number', 'condition', 'value', 'available']


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['customer', 'item', 'borrowed_amount', 'due_date', 'notes']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['loan', 'amount']
