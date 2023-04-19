from django.contrib import admin
from .models import Result, Loan_history_cb, Inquery, CreditBeuro

# Register your models here.
admin.site.register(Result)
admin.site.register(Loan_history_cb)
admin.site.register(Inquery)
admin.site.register(CreditBeuro)
