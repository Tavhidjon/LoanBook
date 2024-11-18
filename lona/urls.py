from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',Temp.as_view(),name='home'),
    path('signup/',RegisterView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),


    path('customers/',CustomerListView.as_view(), name='customer_list'),
    path('customers/<int:pk>/',CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/add/',CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>/edit/',CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete/',CustomerDeleteView.as_view(), name='customer_delete'),

    path('items/',ItemListView.as_view(), name='item_list'),
    path('items/<int:pk>/',ItemDetailView.as_view(), name='item_detail'),
    path('items/add/',ItemCreateView.as_view(), name='item_create'),
    path('items/<int:pk>/edit/',ItemUpdateView.as_view(), name='item_update'),
    path('items/<int:pk>/delete/',ItemDeleteView.as_view(), name='item_delete'),

    path('loans/',LoanListView.as_view(), name='loan_list'),
    path('loans/<int:pk>/',LoanDetailView.as_view(), name='loan_detail'),
    path('loans/add/',LoanCreateView.as_view(), name='loan_create'),
    path('loans/<int:pk>/edit/',LoanUpdateView.as_view(), name='loan_update'),
    path('loans/<int:pk>/delete/',LoanDeleteView.as_view(), name='loan_delete'),

    path('payments/',PaymentListView.as_view(), name='payment_list'),
    path('payments/<int:pk>/',PaymentDetailView.as_view(), name='payment_detail'),
    path('payments/add/',PaymentCreateView.as_view(), name='payment_create'),
    path('payments/<int:pk>/delete/',PaymentDeleteView.as_view(), name='payment_delete'),
]
