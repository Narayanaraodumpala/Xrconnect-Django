# Generated by Django 3.2.9 on 2022-01-06 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0003_alter_session_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='date_modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
