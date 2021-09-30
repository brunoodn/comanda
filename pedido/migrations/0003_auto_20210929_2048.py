# Generated by Django 3.2.7 on 2021-09-29 23:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_alter_pedido_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='status',
        ),
        migrations.AddField(
            model_name='pedido',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='data_criacao',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2021, 9, 29, 23, 48, 59, 166510, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
