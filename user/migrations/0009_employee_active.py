# Generated by Django 3.0.4 on 2020-03-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]