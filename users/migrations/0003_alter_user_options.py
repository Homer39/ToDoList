# Generated by Django 4.2.4 on 2024-07-08 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_username_user_name_alter_user_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]