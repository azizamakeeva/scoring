from django import forms

from .models import Loan, Bail_type, Bail, Repayment_schedule, Loan_history, Aggregated_info, Inquery


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['FCU_code', 'branch', 'loan_type',
                  'type_of_credit', 'purpose_of_funding',
                  'curr', 'interest_rate', 'type_of_repayment',
                  'subtype', 'loan_Stage', 'status',
                  'lender', 'Loan_recipient', 'date_of_issue',
                  'last_update_date', 'next_payment_date',
                  'last_date_of_payment', 'date_of_restructuring',
                  'expected_closing_date', 'actual_closing_date',
                  'main_amount_owed', 'monthly_payment', 'amount_of_credit',
                  'total_amount', 'payment_amount',
                  'count_of_payments', 'calendar', 'payment_intervals', 'amount_written_off',
                  'amount_of_prolongation', 'amount_of_additional_fees',
                  'additional_fees_written_off', 'interest_deducted_amount',
                  'prolongation_date', 'amount_of_delay',
                  'overdue_interest', 'number_of_days_overdue', 'number_of_payments_in_arrears',
                  'bail', 'source']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        form_fields = self.fields

        for field in form_fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class Bail_typeForm(forms.ModelForm):
    class Meta:
        model = Bail_type
        fields = ['bailtype_name']


class BailForm(forms.ModelForm):
    class Meta:
        model = Bail
        fields = ['bail_descr', 'bail_type',
                  'bail_amount', 'collateral_valuation',
                  'collateral_valuation_date', ]


class LoanHistoryForm(forms.ModelForm):
    class Meta:
        model = Loan_history
        fields = [
            'agg_info',
            'date_of_insert',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        form_fields = self.fields

        for field in form_fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class AggInfoForm(forms.ModelForm):
    class Meta:
        model = Aggregated_info
        fields = [
            'inquery', 'request_descr',
            'last_request_to_our_FCU', 'count_of_requests',
            'count_of_delinquencies_on_active_loans',
            'max_current_arrears', 'max_delinquency_per_year',
            'count_of_credits_in_various_FCUs',
            'total_number_of_pledges', 'count_of_connected_subjects',
            'count_of_active_disputes', 'count_of_close_disputes',
            'count_of_requests_per_month', 'count_of_requests_per_in3months',
            'count_of_requests_per_in6months', 'count_of_requests_per_in12months',
            'count_of_requests_per_in24months',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        form_fields = self.fields

        for field in form_fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class InqueryForm(forms.ModelForm):
    class Meta:
        model = Inquery
        fields = ('request_date', 'sector',
                  'reason', 'result', 'belonging_to_the_current_FCU',
                  )


class CalendarForm(forms.ModelForm):
    class Meta:
        model = Repayment_schedule
        fields = ('payment_date', 'amount', 'curr',
                  'overdue_day', 'max_overdue_day',
                  'count_overdue_payments', 'interest_balance',
                  )
