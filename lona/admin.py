from django.contrib import admin


from .models import *



admin.site.register(Item)
admin.site.register(Customer)
admin.site.register(Loan)
admin.site.register(Payment)