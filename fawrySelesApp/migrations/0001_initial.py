# Generated by Django 3.1.5 on 2021-09-27 14:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0003_auto_20210918_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='RassedProtal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(blank=True, null=True, verbose_name='القيمة')),
                ('note', models.TextField(blank=True, max_length=150, null=True, verbose_name='ملاحظات')),
                ('date', models.DateField(default=django.utils.timezone.now, null=True, verbose_name='Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, null=True, verbose_name='Time')),
                ('dateTime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Time')),
            ],
            options={
                'verbose_name': 'رصيد البورتال',
                'verbose_name_plural': 'أرصدة البورتال',
                'ordering': ['-dateTime'],
            },
        ),
        migrations.CreateModel(
            name='TransactionsPortal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(verbose_name='المبلغ')),
                ('isDone', models.BooleanField(blank=True, null=True, verbose_name='انتهاء السداد')),
                ('isDown', models.BooleanField(blank=True, null=True, verbose_name='سداد أم دفع')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('recordDate', models.DateField(default=django.utils.timezone.now, verbose_name='Record Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name='Time')),
                ('dateTime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Time')),
                ('dateTimeProtal', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Time Protal')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='TransactionsPortal.customer+', to='customers.customerinfo', verbose_name='العميل')),
            ],
            options={
                'verbose_name': 'تحويل البورتال',
                'verbose_name_plural': 'سجل التحويلات البورتال',
                'ordering': ['-dateTime'],
            },
        ),
    ]
