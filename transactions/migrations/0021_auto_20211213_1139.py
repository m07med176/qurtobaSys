# Generated by Django 3.1.5 on 2021-12-13 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0020_auto_20211213_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logdate',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 11, 38, 58, 261563), verbose_name='DateTime'),
        ),
    ]
