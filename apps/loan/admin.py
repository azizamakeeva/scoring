from django.contrib import admin
from .models import Bail_type, Bail, Repayment_schedule, Aggregated_info, Loan, Result, Inquery

admin.site.register(Bail_type)
admin.site.register(Bail)
admin.site.register(Repayment_schedule)
admin.site.register(Aggregated_info)
admin.site.register(Loan)
admin.site.register(Result)
admin.site.register(Inquery)
