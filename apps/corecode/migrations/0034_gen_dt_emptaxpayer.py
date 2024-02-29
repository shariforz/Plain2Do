# Generated by Django 4.1.5 on 2024-02-28 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0033_gen_dt_emptaxtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gen_DT_EmpTaxPayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpTaxCategoryCode', models.CharField(max_length=200)),
                ('EmpTaxCategoryEN', models.CharField(max_length=200)),
                ('EmpTaxCategoryRU', models.CharField(max_length=200)),
                ('EmpTaxCategoryTR', models.CharField(max_length=200)),
                ('UniformBaseValueLimitUCVB', models.FloatField(verbose_name='UniformBaseValueLimit(UCVB)')),
                ('WithinLimit', models.FloatField()),
                ('AboveLimit', models.FloatField()),
                ('EmpTaxType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corecode.gen_dt_emptaxtype', verbose_name='Employee Tax Type')),
            ],
            options={
                'ordering': ['EmpTaxCategoryEN'],
            },
        ),
    ]