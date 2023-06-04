from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from django.views.generic.edit import UpdateView

from apps.loan.models import Loan_history
from .forms import ClientForm
from .models import Client


class ClientViewList(ListView):
    def get(self, request):
        clients = Client.objects.all()
        return render(request, 'pages/customer/customer-table.html', {'clients': clients})


class AddClient(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'customer/create.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loan_histories'] = Loan_history.objects.all()
        return context


class ClientDetailView(DetailView):
    model = Client
    # template_name = 'customer/client_detail.html'
    context_object_name = 'client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loan_histories'] = Loan_history.objects.all()
        context['client_list'] = Client.objects.all()
        return context


class UpdateClient(UpdateView):
    form_class = ClientForm
    model = Client
    template_name = 'customer/update.html'

    def get_success_url(self):
        return reverse_lazy('client-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loan_histories'] = Loan_history.objects.all()
        return context


class DeleteClient(DeleteView):
    model = Client
    form_class = ClientForm
    template_name = 'customer/delete.html'
    success_url = '/'


def deleteClient(request, pk):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'customer/delete.html', {'object': client})
