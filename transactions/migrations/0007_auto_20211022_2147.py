# Generated by Django 3.1.5 on 2021-10-22 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_auto_20211022_2145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rest',
            old_name='value',
            new_name='rest',
        ),
    ]
