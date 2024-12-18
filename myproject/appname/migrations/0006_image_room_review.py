# Generated by Django 5.1.1 on 2024-10-01 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0005_alter_reservation_room_alter_reservation_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='../static/images/')),
                ('description', models.CharField(blank=True, max_length=50)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appname.room')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('rating', models.IntegerField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appname.hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appname.user')),
            ],
        ),
    ]
