# Generated by Django 3.1.5 on 2021-10-22 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_record_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rest',
            old_name='value',
            new_name='values',
        ),
    ]
