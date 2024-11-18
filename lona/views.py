from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from .models import Customer, Item, Loan, Payment
from .forms import CustomerForm, ItemForm, LoanForm, PaymentForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages

class Temp(TemplateView):
    template_name = 'home.html'


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    context_object_name = 'customer'


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_form.html'
    success_url = reverse_lazy('customer_list')


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_form.html'
    success_url = reverse_lazy('customer_list')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')


class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'
    context_object_name = 'item'


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('item_list')


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('item_list')


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_confirm_delete.html'
    success_url = reverse_lazy('item_list')


class LoanListView(ListView):
    model = Loan
    template_name = 'loan_list.html'
    context_object_name = 'loans'


class LoanDetailView(DetailView):
    model = Loan
    template_name = 'loan_detail.html'
    context_object_name = 'loan'


class LoanCreateView(CreateView):
    model = Loan
    form_class = LoanForm
    template_name = 'loan_form.html'
    success_url = reverse_lazy('loan_list')


class LoanUpdateView(UpdateView):
    model = Loan
    form_class = LoanForm
    template_name = 'loan_form.html'
    success_url = reverse_lazy('loan_list')


class LoanDeleteView(DeleteView):
    model = Loan
    template_name = 'loan_confirm_delete.html'
    success_url = reverse_lazy('loan_list')


class PaymentListView(ListView):
    model = Payment
    template_name = 'payment_list.html'
    context_object_name = 'payments'


class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'payment_detail.html'
    context_object_name = 'payment'


class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment_form.html'
    success_url = reverse_lazy('payment_list')


class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'payment_confirm_delete.html'
    success_url = reverse_lazy('payment_list')






class RegisterView(TemplateView):
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
        return self.render_to_response({'form': form})
