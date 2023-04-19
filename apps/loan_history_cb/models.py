from django.db import models


class Result(models.Model):
    "Результат"

    result_id = models.AutoField(primary_key=True)
    result = models.CharField(max_length=256, verbose_name='Результат')
    reason = models.CharField(max_length=256, verbose_name='Причина')

    def __str__(self):
        return self.result

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'


class Inquery(models.Model):
    "Запрос"

    inquery_id = models.AutoField(primary_key=True)
    request_date = models.DateField(verbose_name='Дата запроса')
    sector = models.CharField(max_length=256, verbose_name='Сектор')
    reason = models.CharField(max_length=256, verbose_name='Причина')
    result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='Inqueries')
    belonging_to_the_current_FCU = models.IntegerField(verbose_name='Принадлежность к ФКУ')

    def __str__(self):
        return self.inquery_id

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'


class Loan_history_cb(models.Model):
    "Кредитная история с КИБа"

    loan_historycb_id = models.AutoField(primary_key=True)
    inquiery = models.CharField(max_length=255, verbose_name='Запрос')
    Inquiery_last_request_to_our_FCU = models.DateField(verbose_name='последний запрос нашему ФКУ')
    count_requet = models.IntegerField(verbose_name='количество запросов')
    count_of_delinquencies_on_active_loans = models.IntegerField(verbose_name='кол-во просрочек по активным кредитам')
    max_current_arrears = models.IntegerField(verbose_name='макс текущ просрочка ')
    max_current_arrears_year = models.IntegerField(verbose_name='макс просрочка в год')
    count_loan_invarious_FCUs = models.IntegerField(verbose_name='кол-во кредитов в различных ФКУ')
    total_number_of_pledges = models.IntegerField(verbose_name='суммарное кол-во запросов')
    count_of_connected_subjects = models.IntegerField(verbose_name='кол-во связанных субьектов')
    count_of_active_disputes = models.IntegerField(verbose_name='кол-во активных споров')
    count_of_close_disputes = models.IntegerField(verbose_name='кол-во закрытых споров')
    count_of_requests_per_month = models.IntegerField(verbose_name='кол-во запросов за месяц')
    count_of_requests_in3months = models.IntegerField(verbose_name='кол-во запросов за 3 месяца')
    count_of_requests_in6months = models.IntegerField(verbose_name='кол-во запросов за 6 месяца')
    count_of_requests_in12months = models.IntegerField(verbose_name='кол-во запросов за 12 месяца')
    count_of_requests_in24months = models.IntegerField(verbose_name='кол-во запросов за 24 месяца')

    def __str__(self):
        return self.loan_historycb_id

    class Meta:
        verbose_name = 'Кредитная история с киба'
        verbose_name_plural = 'Кредитные истории с киба'


class CreditBeuro(models.Model):
    "Кредитное бюро"

    cb_id = models.AutoField(primary_key=True)
    type_of_credit = models.CharField(max_length=256, verbose_name='Вид кредита')
    purpose_of_funding = models.CharField(max_length=256, verbose_name='Цель финансирования')
    currency_of_the_loan = models.CharField(max_length=64, verbose_name='Валюта кредита')
    type_of_payment = models.CharField(max_length=128, verbose_name='Тип платежа')
    subtypeofcredit = models.CharField(max_length=128, verbose_name='Подвид платежа')
    loan_Stage = models.CharField(max_length=128, verbose_name='Стадия кредита')
    loan_status = models.CharField(max_length=128, verbose_name='Статус кредита')
    lender = models.CharField(max_length=128, verbose_name='Кредитор')
    Loan_recipient = models.CharField(max_length=258, verbose_name='Получатель кредита')
    date_of_issue = models.DateField(verbose_name='Дата выдачи')
    last_upd_date = models.DateField(verbose_name='Последнее обновление')
    next_payment_date = models.DateField(verbose_name='След дата платежа')
    date_of_restructuring = models.DateField(verbose_name='Дата реструктуризации')
    contract_end_date = models.DateField(verbose_name='Дата окончания по договору')
    actual_date_of_credit = models.DateField(verbose_name='Фактич дата погашения')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общ сумма')
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма платежа ')
    total_loan_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общ сумма кредита')
    frequency_of_payments = models.CharField(max_length=64, verbose_name='Периодичность платежей')
    count_of_payments = models.IntegerField(verbose_name='кол-во платежей')
    main_amount_owed = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Осн сумма задолженности')
    amount_monthly_payments = models.DecimalField(max_digits=10, decimal_places=2,
                                                  verbose_name='Сумма месячных платежей')
    Interest_balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='остаток по процентам')
    amount_written_off = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Списанная сумма')
    amount_of_prolongation = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма пролонгации')
    amount_of_additional_fees = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма доп сборов')
    additional_fees_written_off = models.DecimalField(max_digits=10, decimal_places=2,
                                                      verbose_name='Списанные доп сборы')
    interest_deducted_amount = models.DecimalField(max_digits=10, decimal_places=2,
                                                   verbose_name='Списанная сумма по процентам')
    prolongation_date = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='дата пролонгации')
    amount_of_delay = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма просрочки')
    overdue_interest = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='просроченные проценты')
    days_in_arrears = models.IntegerField(verbose_name='дни просрочки')
    count_of_delay = models.IntegerField(verbose_name='кол-во просрочек')
    loah_history = models.ForeignKey(Loan_history_cb, on_delete=models.CASCADE, related_name='CreditBeuro')

    def __str__(self):
        return self.cb_id

    class Meta:
        verbose_name = 'Кредитное бюро'
        verbose_name_plural = 'Кредитные бюро'
