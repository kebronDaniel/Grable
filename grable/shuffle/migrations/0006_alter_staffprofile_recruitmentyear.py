# Generated by Django 3.2.10 on 2021-12-28 14:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shuffle', '0005_staffprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffprofile',
            name='recruitmentYear',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
