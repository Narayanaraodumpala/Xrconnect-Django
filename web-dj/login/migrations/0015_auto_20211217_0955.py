# Generated by Django 3.2.9 on 2021-12-17 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20211217_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionmodel',
            name='created_by',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='sessionmodel',
            name='invited_emails',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
