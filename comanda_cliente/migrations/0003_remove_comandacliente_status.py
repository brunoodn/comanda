# Generated by Django 3.2.7 on 2021-09-29 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comanda_cliente', '0002_alter_comandacliente_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comandacliente',
            name='status',
        ),
    ]
