# Generated by Django 3.1.5 on 2021-12-07 13:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shakawaApp', '0005_auto_20211207_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shakawa',
            name='dateTime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Date Time'),
        ),
    ]
