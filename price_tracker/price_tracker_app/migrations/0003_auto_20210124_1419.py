# Generated by Django 3.1.5 on 2021-01-24 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_tracker_app', '0002_auto_20210124_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snapdeal',
            name='Time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]