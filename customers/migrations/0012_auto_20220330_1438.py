# Generated by Django 3.1.5 on 2022-03-30 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0011_auto_20211222_1443'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customerinfo',
            table='customers_customerinfo',
        ),
        migrations.AlterModelTable(
            name='mandopinfo',
            table='customers_mandopinfo',
        ),
    ]