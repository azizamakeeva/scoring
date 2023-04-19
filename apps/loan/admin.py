from django.contrib import admin
from .models import Bail_type, Bail, Repayment_schedule, Loan_history, Loan

# Register your models here.
admin.site.register(Bail_type)
admin.site.register(Bail)
admin.site.register(Repayment_schedule)
admin.site.register(Loan_history)
admin.site.register(Loan)
