from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from apps.customer.models import Client
from .forms import LoanForm, LoanHistoryForm, AggInfoForm, BailForm, InqueryForm, CalendarForm
from .models import Bail, Bail_type, Repayment_schedule, Loan, Aggregated_info, Loan_history, Inquery, Result


class IndexListView(ListView):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        template_name = 'index.html'
        credit_total = Loan.objects.aggregate(Sum('amount_of_credit'))
        return render(request, template_name, {
            'bail_types': Bail_type.objects.all(),
            'bails': Bail.objects.all(),
            'repayment_schedules': Repayment_schedule.objects.all(),
            'client_count': Client.objects.count(),
            'bail_count': Bail.objects.count(),
            'credit_total': credit_total['amount_of_credit__sum'],
            'inquery_count': Inquery.objects.count(),
        })


class LoanListView(ListView):
    template_name = 'pages/loans/loans-table.html'

    def get(self, request, **kwargs):
        loans = Loan.objects.all()
        return render(request, self.template_name, {'loans': loans})


class LoanDetailView(DetailView):
    model = Loan
    context_object_name = 'loan'
    template_name = 'apps/loans/loan_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Loan_recipient'] = Client.objects.all()
        context['calendars'] = Repayment_schedule.objects.all()
        context['bails'] = Bail.objects.all()
        return context


class AddLoanView(CreateView):
    form_class = LoanForm
    template_name = 'apps/loans/create.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Loan_recipient'] = Client.objects.all()
        context['calendars'] = Repayment_schedule.objects.all()
        context['bails'] = Bail.objects.all()
        return context


class LoanUpdateView(UpdateView):
    form_class = LoanForm
    model = Loan
    template_name = 'apps/loans/update.html'
    success_url = ''


class DeleteLoan(DeleteView):
    model = Loan
    form_class = LoanForm
    success_url = '/'
    template_name = 'apps/loans/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Удаление кредита: {self.object.branch} {self.object.purpose_of_funding}'


class AddLoanHistory(CreateView):
    form_class = LoanHistoryForm
    template_name = 'apps/loan_history/create.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aggregs'] = Aggregated_info.objects.all()
        return context


class LoanHistoryDetailView(DetailView):
    model = Loan_history
    template_name = 'apps/loan_history/loan_history_detail.html'
    context_object_name = 'loan_history'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aggregs'] = Aggregated_info.objects.all()
        return context


class AggListView(ListView):
    template_name = 'pages/loans/agg-table.html'

    def get(self, request, **kwargs):
        aggs = Aggregated_info.objects.all()
        return render(request, self.template_name, {'aggs': aggs})


class AddAgg(CreateView):
    form_class = AggInfoForm
    template_name = 'apps/aggs/create.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inqueris'] = Inquery.objects.all()
        return context


class AggDetailView(DetailView):
    model = Aggregated_info
    context_object_name = 'agg'
    template_name = 'apps/aggs/aggregated_info_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inqueris'] = Inquery.objects.all()
        return context


class AggUpdateView(UpdateView):
    form_class = AggInfoForm
    model = Aggregated_info
    template_name = 'apps/aggs/update.html'
    success_url = reverse_lazy('agglist')


class LoanhistoryListView(ListView):
    template_name = 'pages/loans/loanhistory-table.html'

    def get(self, request, **kwargs):
        loan_histories = Loan_history.objects.all()
        return render(request, self.template_name, {'loan_histories': loan_histories})


class LoanHistoryUpdateView(UpdateView):
    form_class = LoanHistoryForm
    model = Loan_history
    template_name = 'apps/loan_history/update.html'
    success_url = reverse_lazy('historieslist')


class InqueryListView(ListView):
    template_name = 'pages/loans/inquery-table.html'

    def get(self, request, **kwargs):
        inqueries = Inquery.objects.all()
        return render(request, self.template_name, {'inqueries': inqueries})


class AddInquery(CreateView):
    form_class = InqueryForm
    template_name = 'apps/Inquery/create.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['results'] = Result.objects.all()
        return context


class ResultListView(ListView):
    template_name = 'pages/loans/result-table.html'

    def get(self, request, **kwargs):
        results = Result.objects.all()
        return render(request, self.template_name, {'results': results})


class CalendarListView(ListView):
    template_name = 'pages/loans/calendar-table.html'

    def get(self, request, **kwargs):
        calendars = Result.objects.all()
        return render(request, self.template_name, {'calendars': calendars})


class AddCalendar(CreateView):
    form_class = CalendarForm
    template_name = 'apps/calendar/create.html'
    success_url = '/'


class BailListView(ListView):
    template_name = 'pages/loans/bail-table.html'

    def get(self, request, **kwargs):
        bails = Bail.objects.all()
        return render(request, self.template_name, {'bails': bails})


class AddBail(CreateView):
    form_class = BailForm
    template_name = 'apps/bail/create.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bail_types'] = Bail_type.objects.all()
        return context


class BailDetailView(DetailView):
    model = Bail
    template_name = 'apps/bail/bail_detail.html'
    context_object_name = 'bail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bail_types'] = Bail_type.objects.all()
        return context


class BailtypeListView(ListView):
    template_name = 'pages/loans/bailtype-table.html'

    def get(self, request, **kwargs):
        bailtypes = Bail_type.objects.all()
        return render(request, self.template_name, {'bailtypes': bailtypes})
