# Generated by Django 4.1.7 on 2023-05-16 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aggregated_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('request_descr', models.CharField(max_length=128, verbose_name='Запрос')),
                ('last_request_to_our_FCU', models.CharField(max_length=128, verbose_name='Последний запрос нашему ФКУ')),
                ('count_of_requests', models.IntegerField(verbose_name='кол-во запросов')),
                ('count_of_delinquencies_on_active_loans', models.IntegerField(verbose_name='кол-во просрочек по активным кредитам')),
                ('max_current_arrears', models.IntegerField(verbose_name='макс текущ просрочка')),
                ('max_delinquency_per_year', models.IntegerField(verbose_name=' макс просрочка в год')),
                ('count_of_credits_in_various_FCUs', models.IntegerField(verbose_name='кол-во кредитов в различных ФКУ')),
                ('total_number_of_pledges', models.IntegerField(verbose_name='суммарное кол-во залогов')),
                ('count_of_connected_subjects', models.IntegerField(verbose_name='кол-во связанных субьектов')),
                ('count_of_active_disputes', models.IntegerField(verbose_name='кол-во активных споров')),
                ('count_of_close_disputes', models.IntegerField(verbose_name='кол-во закрытых споров')),
                ('count_of_requests_per_month', models.IntegerField(verbose_name='кол-во запроса за месяц')),
                ('count_of_requests_per_in3months', models.IntegerField(verbose_name='кол-во запроса за 3 месяца')),
                ('count_of_requests_per_in6months', models.IntegerField(verbose_name='кол-во запроса за 6 месяца')),
                ('count_of_requests_per_in12months', models.IntegerField(verbose_name='кол-во запроса за 12 месяца')),
                ('count_of_requests_per_in24months', models.IntegerField(verbose_name='кол-во запроса за 24 месяца')),
            ],
            options={
                'verbose_name': 'Кредитная история',
                'verbose_name_plural': 'Кредитные истории',
            },
        ),
        migrations.CreateModel(
            name='Bail',
            fields=[
                ('bail_id', models.AutoField(primary_key=True, serialize=False)),
                ('bail_descr', models.CharField(max_length=256, verbose_name='Описание залога')),
                ('bail_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма залога')),
                ('collateral_valuation', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Оценка залога')),
                ('collateral_valuation_date', models.DateField(verbose_name='Дата оценки залога')),
            ],
            options={
                'verbose_name': 'Залог',
                'verbose_name_plural': 'Залоги',
            },
        ),
        migrations.CreateModel(
            name='Bail_type',
            fields=[
                ('bailtype_id', models.AutoField(primary_key=True, serialize=False)),
                ('bailtype_name', models.CharField(max_length=256, verbose_name='Тип залога')),
            ],
            options={
                'verbose_name': 'Тип залога',
                'verbose_name_plural': 'Типы залогов',
            },
        ),
        migrations.CreateModel(
            name='Repayment_schedule',
            fields=[
                ('repaymentschedule_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_date', models.DateField(verbose_name='Дата платежа')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма')),
                ('curr', models.CharField(max_length=64, verbose_name='Валюта')),
                ('overdue_day', models.BooleanField(verbose_name='Просроченный день')),
                ('max_overdue_day', models.IntegerField(verbose_name='Макс просроченный день')),
                ('count_overdue_payments', models.IntegerField(verbose_name='кол-во просроченных платежей')),
                ('interest_balance', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='остаток по процентам')),
            ],
            options={
                'verbose_name': 'Календарь погашений',
                'verbose_name_plural': 'Календари погашений',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('result', models.CharField(max_length=256, verbose_name='Результат')),
                ('reason', models.CharField(max_length=256, verbose_name='Причина')),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результаты',
            },
        ),
        migrations.CreateModel(
            name='Loan_history',
            fields=[
                ('loanhistory_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_insert', models.DateField()),
                ('agg_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_history_agg', to='loan.aggregated_info')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('FCU_code', models.IntegerField(verbose_name='Код ФКУ')),
                ('branch', models.CharField(max_length=155, verbose_name='Филиал')),
                ('loan_type', models.CharField(max_length=155, verbose_name='Тип кредита')),
                ('type_of_credit', models.CharField(max_length=256, verbose_name='Вид кредита')),
                ('purpose_of_funding', models.CharField(max_length=256, verbose_name='Цель финансирования')),
                ('curr', models.CharField(max_length=64, verbose_name='Валюта')),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Процентная ставка')),
                ('type_of_repayment', models.CharField(max_length=128, verbose_name='Тип погашения')),
                ('subtype', models.CharField(max_length=128, verbose_name='Субтип')),
                ('loan_Stage', models.CharField(max_length=128, verbose_name='Стадия кредита')),
                ('status', models.CharField(max_length=64, verbose_name='Статус')),
                ('lender', models.CharField(max_length=128, verbose_name='Кредитор')),
                ('date_of_issue', models.DateField(verbose_name='Дата выдачи')),
                ('last_update_date', models.DateField(verbose_name='Посл дата обновления')),
                ('next_payment_date', models.DateField(verbose_name='След дата платежа')),
                ('last_date_of_payment', models.DateField(verbose_name='Посл дата платежа')),
                ('date_of_restructuring', models.DateField(verbose_name='Дата реструктуризации')),
                ('expected_closing_date', models.DateField(verbose_name='Ожидаемая дата закрытия')),
                ('actual_closing_date', models.DateField(verbose_name='Действительная дата закрытия')),
                ('main_amount_owed', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Осн сумма задолженности')),
                ('monthly_payment', models.CharField(max_length=128, verbose_name='Ежемесечная выплата')),
                ('amount_of_credit', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма кредита')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Общ сумма')),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма платежа')),
                ('frequency_of_payments', models.CharField(max_length=64, verbose_name='Периодичность платежей')),
                ('count_of_payments', models.IntegerField(verbose_name='кол-во платежей')),
                ('payment_intervals', models.CharField(max_length=128, verbose_name='Периодичность платежей')),
                ('amount_monthly_payments', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма месячных платежей')),
                ('amount_written_off', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Списанная сумма')),
                ('amount_of_prolongation', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма пролонгации')),
                ('amount_of_additional_fees', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма доп сборов')),
                ('additional_fees_written_off', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Списанные доп сборы')),
                ('interest_deducted_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Списанная сумма по процентам')),
                ('prolongation_date', models.DateField(verbose_name='дата пролонгации')),
                ('number_of_payments', models.IntegerField(verbose_name='Кол-во платежей')),
                ('amount_of_delay', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма просрочки')),
                ('overdue_interest', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='просроченные проценты')),
                ('number_of_days_overdue', models.IntegerField(verbose_name='Кол-во дней просрочек')),
                ('number_of_payments_in_arrears', models.IntegerField(verbose_name='Кол-во платежей в просрочке ')),
                ('source', models.CharField(max_length=155, verbose_name='')),
                ('Loan_recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_client', to='customer.client', verbose_name='Получатель кредита')),
                ('bail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans_bail', to='loan.bail')),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans_calendar', to='loan.repayment_schedule')),
            ],
            options={
                'verbose_name': 'Кредит',
                'verbose_name_plural': 'Кредиты',
            },
        ),
        migrations.CreateModel(
            name='Inquery',
            fields=[
                ('inquery_id', models.AutoField(primary_key=True, serialize=False)),
                ('request_date', models.DateField(verbose_name='Дата запроса')),
                ('sector', models.CharField(max_length=256, verbose_name='Сектор')),
                ('reason', models.CharField(max_length=256, verbose_name='Причина')),
                ('belonging_to_the_current_FCU', models.IntegerField(verbose_name='Принадлежность к ФКУ')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Inqueries', to='loan.result')),
            ],
            options={
                'verbose_name': 'Запрос',
                'verbose_name_plural': 'Запросы',
            },
        ),
        migrations.AddField(
            model_name='bail',
            name='bail_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bails', to='loan.bail_type'),
        ),
        migrations.AddField(
            model_name='aggregated_info',
            name='inquery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.inquery'),
        ),
        migrations.AddField(
            model_name='aggregated_info',
            name='loan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.loan'),
        ),
    ]
