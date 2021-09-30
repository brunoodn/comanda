# Generated by Django 3.2.7 on 2021-09-29 23:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comanda_cliente', '0003_remove_comandacliente_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='comandacliente',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comandacliente',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 9, 29, 23, 34, 8, 412093, tzinfo=utc)),
            preserve_default=False,
        ),
    ]