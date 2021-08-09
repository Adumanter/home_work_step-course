# Generated by Django 3.2.6 on 2021-08-08 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200, verbose_name='Имя пользователя')),
                ('user_phone', models.CharField(max_length=200, verbose_name='Номер телефона')),
                ('user_email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('user_comment', models.TextField(verbose_name='Комментарий')),
            ],
        ),
    ]
