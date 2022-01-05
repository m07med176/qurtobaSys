# Generated by Django 3.1.5 on 2021-12-28 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100, verbose_name='UID')),
                ('email', models.CharField(max_length=100, verbose_name='الايميل')),
                ('name', models.CharField(max_length=30, verbose_name='الإسم')),
                ('day', models.DateField(blank=True, null=True, verbose_name='اليوم')),
                ('startTime', models.TimeField(blank=True, null=True, verbose_name='بداية اليوم')),
                ('endTime', models.TimeField(blank=True, null=True, verbose_name='نهاية اليوم')),
                ('duration', models.TimeField(blank=True, null=True, verbose_name='الفترة')),
                ('dateTime', models.DateTimeField(blank=True, default=datetime.datetime.today, null=True, verbose_name='Date Time')),
                ('transport', models.FloatField(blank=True, default=0, null=True, verbose_name='تكلفة المواصلات')),
                ('notes', models.TextField(blank=True, default='', null=True, verbose_name='الملاحظات')),
                ('is_active', models.BooleanField(default=False, verbose_name='متاح')),
            ],
            options={
                'verbose_name': 'متابعه',
                'verbose_name_plural': 'المتابعات',
                'ordering': ['-dateTime'],
            },
        ),
    ]