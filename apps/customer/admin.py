from django.contrib import admin
from .models import Client, Loan_history

# Register your models here.
admin.site.register(Client)
admin.site.register(Loan_history)
