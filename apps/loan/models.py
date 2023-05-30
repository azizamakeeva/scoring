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
    result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='Inqueries', null=True, blank=True)
    belonging_to_the_current_FCU = models.IntegerField(verbose_name='Принадлежность к ФКУ')

    def __str__(self):
        return self.reason

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'


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
    """Залог"""

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
    """Календарь погашений"""

    repaymentschedule_id = models.AutoField(primary_key=True)
    payment_date = models.DateField(verbose_name='Дата платежа')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    curr = models.CharField(max_length=64, verbose_name='Валюта')
    overdue_day = models.BooleanField(verbose_name='Просроченный день')
    max_overdue_day = models.IntegerField(verbose_name='Макс просроченный день')
    count_overdue_payments = models.IntegerField(verbose_name='кол-во просроченных платежей')
    interest_balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='остаток по процентам')

    class Meta:
        verbose_name = 'Календарь погашений'
        verbose_name_plural = 'Календари погашений'

    def __str__(self):
        return f'{self.payment_date} | {self.amount} {self.curr}'


class Loan(models.Model):
    """Кредит"""

    'Детали кредита'
    loan_id = models.AutoField(primary_key=True)
    FCU_code = models.IntegerField(verbose_name='Код ФКУ')
    branch = models.CharField(max_length=155, verbose_name='Филиал')
    loan_type = models.CharField(max_length=155, verbose_name='Тип кредита')
    type_of_credit = models.CharField(max_length=256, verbose_name='Вид кредита')
    purpose_of_funding = models.CharField(max_length=256, verbose_name='Цель финансирования')
    curr = models.CharField(max_length=64, verbose_name='Валюта')
    interest_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Процентная ставка')
    type_of_repayment = models.CharField(max_length=128, verbose_name='Тип погашения')
    subtype = models.CharField(max_length=128, verbose_name='Субтип')
    loan_Stage = models.CharField(max_length=128, verbose_name='Стадия кредита')
    status = models.CharField(max_length=64, verbose_name='Статус')
    lender = models.CharField(max_length=128, verbose_name='Кредитор')
    Loan_recipient = models.ForeignKey('customer.Client', on_delete=models.CASCADE, related_name='loan_client',
                                       verbose_name='Получатель кредита')
    'Ключевые даты'
    date_of_issue = models.DateField(verbose_name='Дата выдачи', null=True, blank=True)
    last_update_date = models.DateField(verbose_name='Посл дата обновления', null=True, blank=True)
    next_payment_date = models.DateField(verbose_name='След дата платежа', null=True, blank=True)
    last_date_of_payment = models.DateField(verbose_name='Посл дата платежа', null=True, blank=True)
    date_of_restructuring = models.DateField(verbose_name='Дата реструктуризации', null=True, blank=True)
    expected_closing_date = models.DateField(verbose_name='Ожидаемая дата закрытия', null=True, blank=True)
    actual_closing_date = models.DateField(verbose_name='Действительная дата закрытия', null=True, blank=True)

    main_amount_owed = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Осн сумма задолженности')
    monthly_payment = models.CharField(max_length=128, verbose_name='Ежемесечная выплата', null=True, blank=True)
    amount_of_credit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма кредита', null=True,
                                           blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общ сумма', null=True, blank=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма платежа', null=True,
                                         blank=True)
    frequency_of_payments = models.CharField(max_length=64, verbose_name='Периодичность платежей', null=True,
                                             blank=True)
    count_of_payments = models.IntegerField(verbose_name='кол-во платежей', null=True, blank=True)

    calendar = models.ForeignKey(Repayment_schedule, on_delete=models.CASCADE, related_name='loans_calendar', null=True,
                                 blank=True)
    payment_intervals = models.CharField(max_length=128, verbose_name='Периодичность платежей', null=True, blank=True)
    amount_written_off = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Списанная сумма', null=True,
                                             blank=True)
    amount_of_prolongation = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма пролонгации',
                                                 null=True, blank=True)
    amount_of_additional_fees = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма доп сборов',
                                                    null=True, blank=True)
    additional_fees_written_off = models.DecimalField(max_digits=10, decimal_places=2,
                                                      verbose_name='Списанные доп сборы', null=True, blank=True)
    interest_deducted_amount = models.DecimalField(max_digits=10, decimal_places=2,
                                                   verbose_name='Списанная сумма по процентам', null=True, blank=True)
    prolongation_date = models.DateField(verbose_name='дата пролонгации', null=True, blank=True)

    amount_of_delay = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма просрочки', null=True,
                                          blank=True)
    overdue_interest = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='просроченные проценты',
                                           null=True, blank=True)
    number_of_days_overdue = models.IntegerField(verbose_name='Кол-во дней просрочек', null=True, blank=True)
    number_of_payments_in_arrears = models.IntegerField(verbose_name='Кол-во платежей в просрочке ', null=True,
                                                        blank=True)

    bail = models.ForeignKey(Bail, on_delete=models.CASCADE, related_name='loans_bail')
    source = models.CharField(verbose_name='Источник', max_length=155)

    def __str__(self):
        return self.purpose_of_funding

    class Meta:
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'


class Aggregated_info(models.Model):
    """ Кредитная история, агрегированные данные """

    id = models.AutoField(primary_key=True)
    inquery = models.ForeignKey(Inquery, on_delete=models.CASCADE)
    request_descr = models.CharField(max_length=128, verbose_name='Запрос')
    last_request_to_our_FCU = models.DateField(max_length=128, verbose_name='Последний запрос нашему ФКУ')
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
        verbose_name = 'Агрегированная информация'
        verbose_name_plural = 'Агрегированные данные'

    def __str__(self):
        return self.request_descr


class Loan_history(models.Model):
    loanhistory_id = models.AutoField(primary_key=True)
    agg_info = models.ForeignKey(Aggregated_info, on_delete=models.CASCADE, related_name='loan_history_agg')
    date_of_insert = models.DateField()

    class Meta:
        verbose_name = 'Кредитная история'
        verbose_name_plural = 'Кредитные истории'

    def __str__(self):
        return f'{self.agg_info} | {self.date_of_insert}'
