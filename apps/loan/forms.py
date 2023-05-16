from django import forms

from .models import Loan, Bail_type, Bail, Repayment_schedule, Loan_history


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ('FCU_code', 'loan_history',
                  'branch', 'loan_type',
                  'destination', 'curr',
                  'type_of_repayment',
                  'subtype', 'status',
                  'date_of_issue', 'last_update_date',
                  'last_date_of_payment', 'date_of_restructuring',
                  'expected_closing_date', 'actual_closing_date',
                  'amount_of_credit', 'calendar',
                  'monthly_payment', 'payment_intervals',
                  'bail', 'number_of_payments',
                  'number_of_days_overdue', 'number_of_payments_in_arrears')


class Bail_typeForm(forms.ModelForm):
    class Meta:
        model = Bail_type
        fields = ['bailtype_name']


class BailForm(forms.ModelForm):
    class Meta:
        model = Bail
        fields = ['bail_descr', 'bail_type', 'bail_amount', 'collateral_valuation', 'collateral_valuation_date']


class Repayment_scheduleForm(forms.ModelForm):
    class Meta:
        model = Repayment_schedule
        fields = ['repaymentschedule_id', 'payment_date', 'amount', 'curr', 'overdue_day', 'max_overdue_day',
                  'count_overdue_payments', 'Interest_rate', ]


class LoanHistoryForm(forms.ModelForm):
    class Meta:
        model: Loan_history
        fields = [
            'request_descr', 'last_request_to_our_FCU',
            'count_of_requests', 'count_of_delinquencies_on_active_loans',
            'max_current_arrears', 'max_delinquency_per_year',
            'count_of_credits_in_various_FCUs', 'total_number_of_pledges',
            'count_of_connected_subjects', 'count_of_active_disputes', 'count_of_close_disputes',
            'count_of_requests_per_month', 'count_of_requests_per_in3months',
            'count_of_requests_per_in6months', 'count_of_requests_per_in12months',
            'count_of_requests_per_in24months',
        ]
