# Generated by Django 3.2.9 on 2022-01-04 10:22

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('login', '0024_alter_registermodel_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='registermodel',
            table='login.users',
        ),
    ]
