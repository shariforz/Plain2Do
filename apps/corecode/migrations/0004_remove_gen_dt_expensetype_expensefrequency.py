# Generated by Django 5.0.4 on 2024-05-24 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0003_alter_gen_dt_budgetdata_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gen_dt_expensetype',
            name='ExpenseFrequency',
        ),
    ]
