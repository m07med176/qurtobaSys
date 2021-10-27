# Generated by Django 3.1.5 on 2021-10-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0010_auto_20211023_0306'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='rest',
            field=models.FloatField(default=0, verbose_name='المتبقى'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rest',
            name='type',
            field=models.IntegerField(choices=[(0, 'متبقيات'), (1, 'مدفوعات')], default=0, verbose_name=' النوع '),
        ),
    ]
