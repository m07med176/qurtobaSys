# Generated by Django 3.1.5 on 2021-12-13 09:12

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0018_auto_20211212_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name='Time')),
                ('datetime', models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name='DateTime')),
            ],
            options={
                'verbose_name': 'سجل التاريخ',
                'verbose_name_plural': 'سجلات التواريخ',
                'ordering': ['-datetime'],
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='record',
            name='type',
            field=models.CharField(choices=[('فورى', 'فورى'), ('كاش', 'كاش'), ('طاير', 'طاير'), ('بى', 'بى'), ('أمان', 'أمان'), ('أخرى', 'أخرى'), ('تنزيل', 'تنزيل'), ('تحصيل', 'تحصيل'), ('شراء', 'شراء'), ('الدفع', 'الدفع')], default=1, max_length=50, verbose_name='نوع الحساب'),
        ),
    ]
