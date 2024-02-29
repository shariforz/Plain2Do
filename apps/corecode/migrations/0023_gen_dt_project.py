# Generated by Django 4.1.5 on 2024-02-28 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0022_gen_dt_subjectofrf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gen_DT_Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectID_1C', models.CharField(max_length=100)),
                ('ProjectCode', models.CharField(max_length=200)),
                ('ProjectNameEN', models.CharField(max_length=200)),
                ('ProjectNameRU', models.CharField(max_length=200)),
                ('ProjectNameTR', models.CharField(max_length=200)),
                ('AddressEN', models.CharField(max_length=200)),
                ('AddressRU', models.CharField(max_length=200)),
                ('AddressTR', models.CharField(max_length=200)),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('SubjectofRF', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corecode.gen_dt_subjectofrf', verbose_name='Subject of RF')),
            ],
            options={
                'ordering': ['ProjectNameEN'],
            },
        ),
    ]