# Generated by Django 5.1.1 on 2024-10-08 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0010_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
