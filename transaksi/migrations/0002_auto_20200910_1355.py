# Generated by Django 2.2 on 2020-09-10 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaksi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaksi',
            name='waktu',
            field=models.DateField(default=datetime.datetime),
        ),
    ]
