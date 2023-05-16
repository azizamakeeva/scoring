# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from django.views.generic.list import ListView
# from .forms import LoanForm, Bail_typeForm, BailForm, Repayment_scheduleForm, LoanHistoryForm
# from .models import Bail, Bail_type, Repayment_schedule, Loan, Aggregated_info
# from django.shortcuts import redirect
#
#
# #
# def create_bailtype(request):
#     if request.method == "POST":
#         form = Bail_typeForm(request.POST)
#         if form.is_valid():
#             bail_type = form.save(commit=False)
#             bail_type.save()
#             return redirect('index')
#     else:
#         form = Bail_typeForm()
#
#     return render(request, "loan/bail_type.html", {"form": form})
#
#
# def create_bail(request):
#     bailtypes = Bail_type.objects.all()
#     if request.method == "POST":
#         form = BailForm(request.POST)
#         if form.is_valid():
#             bail_type = form.save(commit=False)
#             bail_type.save()
#             return redirect('index')
#
#     else:
#         form = BailForm()
#
#     return render(request, "loan/bail_create.html", {"form": form, 'bailtypes': bailtypes})
#
#
# def create_loan(request):
#     loans = Loan.objects.all()
#     loan_histories = Aggregated_info.objects.all()
#     calendars = Repayment_schedule.objects.all()
#     bails = Bail.objects.all()
#     if request.method == "POST":
#         form = LoanForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')  # ?
#     else:
#         form = LoanForm()
#
#     return render(request, "loan/loan_create.html",
#                   {"form": form, 'loans': loans, 'loan_histories': loan_histories, 'calendars': calendars,
#                    'bails': bails})
#
#
# def create_repaymentschedule(request):
#     repaymentschedule = Repayment_schedule.objects.all()
#     if request.method == 'POST':
#         form = Repayment_scheduleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = Repayment_scheduleForm()
#     return render(request, "loan/repaymentschedule_create.html",
#                   {"form": form, "repaymentschedule": repaymentschedule})
#
#
# def create_loanhistory(request):
#     loanhistory = Aggregated_info.objects.all()
#     if request.method == "POST":
#         form = LoanHistoryForm(request.POST)
#         if form.is_valid():
#             loanhistory = form.save(commit=False)
#             loanhistory.save()
#             return redirect('index')  # ?
#     else:
#         form = LoanHistoryForm()
#
#     return render(request, "loan/loanHistory.html",
#                   {"form": form, 'loanhistory': loanhistory})
#
#
# class BailListView(ListView):
#     model = Bail
#     template_name = 'index.html'
#     context_object_name = 'bails'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['section'] = 'featured'  # добавляем новый ключ в контекст данных
#         return context
#
#
# class ModelsListView(ListView):
#     template_name = 'index.html'
#
#     def index(request):
#         return render(request, 'index.html')
#
#     def get_queryset(self):
#         return {
#             'bail_types': Bail_type.objects.all(),
#             'bails': Bail.objects.all(),
#             'repayment_schedules': Repayment_schedule.objects.all(),
#         }
#
#
# class LoanListView(ListView):
#     template_name = 'pages/loans/loans-table.html'
#
#     def get(self, request):
#         loans = Loan.objects.all()
#         return render(request, self.template_name, {'loans': loans})
