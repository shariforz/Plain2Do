# Generated by Django 4.1.5 on 2023-01-30 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_position_alter_student_current_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='position',
            field=models.CharField(max_length=200, verbose_name='Должность'),
        ),
    ]