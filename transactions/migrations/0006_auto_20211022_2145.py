# Generated by Django 3.1.5 on 2021-10-22 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_auto_20211022_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rest',
            old_name='values',
            new_name='value',
        ),
    ]
