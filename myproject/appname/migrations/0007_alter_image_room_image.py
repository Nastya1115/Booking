# Generated by Django 5.1.1 on 2024-10-01 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0006_image_room_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_room',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
