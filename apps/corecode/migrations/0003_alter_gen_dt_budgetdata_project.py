# Generated by Django 5.0.4 on 2024-05-21 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0002_alter_gen_dt_budgetdata_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gen_dt_budgetdata',
            name='Project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='corecode.gen_dt_project'),
        ),
    ]
