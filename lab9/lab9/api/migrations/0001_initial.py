# Generated by Django 3.1.7 on 2021-04-15 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('address', models.TextField(verbose_name='Адрес')),
            ],
        ),
        migrations.CreateModel(
            name='vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
                ('salary', models.FloatField(verbose_name='Зарплата')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
    ]
