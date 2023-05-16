from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from apps.loan.models import Loan_history
from .forms import ClientForm
from django.shortcuts import redirect
from django.views.generic.list import ListView
from .models import Client


class ClientViewList(ListView):
    def get(self, request):
        clients = Client.objects.all()
        return render(request, 'pages/customer/customer-table.html', {'clients': clients})

    def create_client(request):
        loan_histories = Loan_history.objects.all()
        if request.method == "POST":
            form = ClientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')  # ?

        else:
            form = ClientForm()

        return render(request, "customer/create.html",
                      {"form": form, "loan_histories": loan_histories, "loan_histories_cb": loan_histories_cb})
