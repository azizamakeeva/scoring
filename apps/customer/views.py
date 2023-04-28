from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from apps.loan.models import Loan_history
from apps.loan_history_cb.models import Loan_history_cb
from .forms import ClientForm
from django.shortcuts import redirect


def create_client(request):
    loan_histories = Loan_history.objects.all()
    loan_histories_cb = Loan_history_cb.objects.all()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')  # ?

    else:
        form = ClientForm()

    return render(request, "customer/create.html",
                  {"form": form, "loan_histories": loan_histories, "loan_histories_cb": loan_histories_cb})
