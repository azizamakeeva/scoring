# Generated by Django 4.1.7 on 2023-05-30 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_remove_loan_number_of_payments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='frequency_of_payments',
        ),
    ]
