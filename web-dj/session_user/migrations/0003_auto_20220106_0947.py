# Generated by Django 3.2.9 on 2022-01-06 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session_user', '0002_alter_session_users_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session_users',
            name='is_favourite',
        ),
        migrations.RemoveField(
            model_name='session_users',
            name='user_avatar',
        ),
    ]
