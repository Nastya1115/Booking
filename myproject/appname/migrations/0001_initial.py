# Generated by Django 5.1.1 on 2024-09-17 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('room_type', models.CharField(max_length=20)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appname.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation', models.IntegerField(auto_created=True, unique=True)),
                ('reservation_start', models.DateField()),
                ('reservation_end', models.DateField()),
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appname.room')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appname.user')),
            ],
        ),
    ]
