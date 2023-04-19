from django.db import models


# Create your models here.
class Bail_type(models.Model):
    "Тип залога"

    bailtype_id = models.AutoField(primary_key=True)
    bailtype_name = models.CharField(max_length=256, verbose_name='Тип залога')

    def __str__(self):
        return self.bailtype_name

    class Meta:
        verbose_name = 'Тип залога'
        verbose_name_plural = 'Типы залогов'


class Bail(models.Model):
    "Залог"

    bail_id = models.AutoField(primary_key=True)
    bail_descr = models.CharField(max_length=256, verbose_name='Описание залога')
    bail_type = models.ForeignKey(Bail_type, on_delete=models.CASCADE, related_name='bails')
    bail_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма залога')
    collateral_valuation = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Оценка залога')
    collateral_valuation_date = models.DateField(verbose_name='Дата оценки залога')

    def __str__(self):
        return self.bail_descr

    class Meta:
        verbose_name = 'Залог'
        verbose_name_plural = 'Залоги'


class Repayment_schedule(models.Model):
    "Календарь погашений"

    repaymentschedule_id = models.AutoField(primary_key=True)
    payment_date = models.DateField(verbose_name='Дата платежа')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    curr = models.CharField(max_length=64, verbose_name='Валюта')
    overdue_day = models.BooleanField(verbose_name='Просроченный день')
    max_overdue_day = models.IntegerField(verbose_name='Макс просроченный день')
    count_overdue_payments = models.IntegerField(verbose_name='кол-во просроченных платежей')
    Interest_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Процентная ставка')


    class Meta:
        verbose_name = 'Календарь погашений'
        verbose_name_plural = 'Календари погашений'

class Loan_history(models.Model):
    " Кредитная история"

    loanhistory_id = models.AutoField(primary_key=True)
    request_descr = models.CharField(max_length=128, verbose_name='Запрос')
    last_request_to_our_FCU = models.CharField(max_length=128, verbose_name='Последний запрос нашему ФКУ')
    count_of_requests = models.IntegerField(verbose_name='кол-во запросов')
    count_of_delinquencies_on_active_loans = models.IntegerField(verbose_name='кол-во просрочек по активным кредитам')
    max_current_arrears = models.IntegerField(verbose_name='макс текущ просрочка')
    max_delinquency_per_year = models.IntegerField(verbose_name=' макс просрочка в год')
    count_of_credits_in_various_FCUs = models.IntegerField(verbose_name='кол-во кредитов в различных ФКУ')
    total_number_of_pledges = models.IntegerField(verbose_name='суммарное кол-во залогов')
    count_of_connected_subjects = models.IntegerField(verbose_name='кол-во связанных субьектов')
    count_of_active_disputes = models.IntegerField(verbose_name='кол-во активных споров')
    count_of_close_disputes = models.IntegerField(verbose_name='кол-во закрытых споров')
    count_of_requests_per_month = models.IntegerField(verbose_name='кол-во запроса за месяц')
    count_of_requests_per_in3months = models.IntegerField(verbose_name='кол-во запроса за 3 месяца')
    count_of_requests_per_in6months = models.IntegerField(verbose_name='кол-во запроса за 6 месяца')
    count_of_requests_per_in12months = models.IntegerField(verbose_name='кол-во запроса за 12 месяца')
    count_of_requests_per_in24months = models.IntegerField(verbose_name='кол-во запроса за 24 месяца')

    class Meta:
        verbose_name = 'Кредитная история'
        verbose_name_plural = 'Кредитные истории'

class Loan(models.Model):
    'Кредит'

    loan_id = models.AutoField(primary_key=True)
    FCU_code = models.IntegerField(verbose_name='Код ФКУ')
    loan_history = models.ForeignKey(Loan_history, on_delete=models.CASCADE, related_name='loans_hisory')
    branch = models.CharField(max_length=155, verbose_name='Филиал')
    loan_type = models.CharField(max_length=155, verbose_name='Тип кредита')
    destination = models.CharField(max_length=255, verbose_name='Назначение')
    curr = models.CharField(max_length=64, verbose_name='Валюта')
    type_of_repayment = models.CharField(max_length=128, verbose_name='Тип погашения')
    subtype = models.CharField(max_length=128, verbose_name='Субтип')
    status = models.CharField(max_length=64, verbose_name='Статус')
    date_of_issue = models.DateField(verbose_name='Дата выдачи')
    last_update_date = models.DateField(verbose_name='Посл дата обновления')
    last_date_of_payment = models.DateField(verbose_name='Посл дата платежа')
    date_of_restructuring = models.DateField(verbose_name='Дата реструктуризации')
    expected_closing_date = models.DateField(verbose_name='Ожидаемая дата закрытия')
    actual_closing_date = models.DateField(verbose_name='Действительная дата закрытия')
    amount_of_credit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма кредита')
    calendar = models.ForeignKey(Repayment_schedule, on_delete=models.CASCADE, related_name='loans_calendar')
    monthly_payment = models.CharField(max_length=128, verbose_name='Ежемесечная выплата')
    payment_intervals = models.CharField(max_length=128, verbose_name='Периодичность платежей')
    bail = models.ForeignKey(Bail, on_delete=models.CASCADE, related_name='loans_bail')
    number_of_payments = models.IntegerField(verbose_name='Кол-во платежей')
    number_of_days_overdue = models.IntegerField(verbose_name='Кол-во дней просрочек')
    number_of_payments_in_arrears = models.IntegerField(verbose_name='Кол-во платежей в просрочке ')

    def __str__(self):
        return self.loan_id

    class Meta:
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'
