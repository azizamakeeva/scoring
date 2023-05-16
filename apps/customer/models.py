from django.db import models
from apps.loan.models import Aggregated_info,Loan_history

SEX_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male')
)


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, verbose_name='Имя')
    lastname = models.CharField(max_length=128, verbose_name='Фамилия')
    fatherstname = models.CharField(max_length=64, verbose_name='Отчество')
    dateofbirth = models.DateField(verbose_name='Дата рождения')
    sex = models.CharField(max_length=16, choices=SEX_CHOICES)
    сitizenship = models.CharField(max_length=155, verbose_name='Гражданство')
    inn = models.CharField(max_length=64, verbose_name='ИНН')
    document_number = models.CharField(max_length=64, verbose_name='Номер документа')
    expiration_date = models.DateField(verbose_name='срок действия')
    date_of_issue = models.DateField(verbose_name='дата выдачи')
    distribution_organization = models.CharField(max_length=256, verbose_name='орган выдачи')
    address = models.CharField(max_length=256, verbose_name='Адрес')
    Occupation = models.CharField(max_length=256, verbose_name='Род деятельности')
    family_status = models.CharField(max_length=256, verbose_name='Семейное положение')
    contact = models.CharField(max_length=256, verbose_name='Контакты')
    loan_history = models.ForeignKey(Loan_history, on_delete=models.CASCADE, related_name='client_lh')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


