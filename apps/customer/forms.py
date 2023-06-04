from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'lastname',
                  'fatherstname', 'dateofbirth',
                  'sex', 'сitizenship',
                  'inn', 'document_number',
                  'expiration_date', 'date_of_issue',
                  'distribution_organization', 'address',
                  'Occupation', 'family_status',
                  'contact', 'loan_history', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        form_fields = self.fields

        for field in form_fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
