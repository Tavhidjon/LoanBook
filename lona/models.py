from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from decimal import Decimal


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    id_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    serial_number = models.CharField(max_length=50, unique=True)
    condition = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"


class Loan(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('OVERDUE', 'Overdue'),
        ('RETURNED', 'Returned'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    loan_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE')
    borrowed_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    remaining_balance = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def save(self, *args, **kwargs):
        self.remaining_balance = Decimal(self.borrowed_amount) - Decimal(self.amount_paid)
        if self.status == 'ACTIVE' and self.due_date < timezone.now():
            self.status = 'OVERDUE'
        if self.remaining_balance <= 0:
            self.status = 'RETURNED'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.item.name} - {self.customer.name}"





class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.loan.amount_paid += self.amount
        self.loan.save()

    def __str__(self):
        return f"Payment of {self.amount} for {self.loan}"
