# Generated by Django 3.0.4 on 2020-03-22 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_employee_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='probation_period',
            field=models.IntegerField(choices=[(0, 'No Probation'), (1, '1 Month'), (3, '3 Months'), (6, '6 Months'), (8, '8 Months'), (12, '1 Year'), (18, '1.5 years')], default=3),
        ),
    ]