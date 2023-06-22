from django.contrib import admin

# Register your models here.
from.models import Payment
class PaymentAdmin(admin.ModelAdmin):
    payments = ("amount","payment_method","date","receipt","status","order")
    admin.site.register(Payment)
