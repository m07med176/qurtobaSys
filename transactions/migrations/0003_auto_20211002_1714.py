# Generated by Django 3.1.5 on 2021-10-02 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20210927_1626'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talabat',
            options={'ordering': ['-dateTime'], 'verbose_name': 'طلب', 'verbose_name_plural': 'سجل الطلبات'},
        ),
    ]