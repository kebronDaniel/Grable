# Generated by Django 3.2.10 on 2022-01-06 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuffle', '0009_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='location',
            field=models.TextField(default=''),
        ),
    ]