# Generated by Django 5.1.1 on 2024-09-24 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0002_rename_reservations_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='appname.hotel'),
        ),
    ]
