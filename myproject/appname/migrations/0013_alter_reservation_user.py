# Generated by Django 5.1.1 on 2024-10-15 16:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0012_rename_location_hotel_description_room_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
