# Generated by Django 2.2.6 on 2019-10-20 11:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20191020_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='txn_type',
            field=models.CharField(choices=[('A', 'Paid by Credit Card'), ('B', 'Paid by Debit Card'), ('C', 'Cash Transfer')], default='A', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 20, 16, 31, 42, 935983)),
        ),
    ]