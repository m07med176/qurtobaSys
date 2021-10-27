# Generated by Django 3.1.5 on 2021-07-04 07:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FawryCodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceName', models.CharField(max_length=100, verbose_name='إسم الخدمة')),
                ('serviceCode', models.CharField(max_length=100, verbose_name='كود الخدمة')),
                ('serviceKind', models.CharField(max_length=100, verbose_name='نوع الخدمة')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='DateTime')),
                ('date', models.DateField(default=django.utils.timezone.now, null=True, verbose_name='التاريخ')),
                ('time', models.TimeField(default=django.utils.timezone.now, null=True, verbose_name='الوقت')),
            ],
            options={
                'verbose_name': 'كود فورى',
                'verbose_name_plural': 'أكواد فورى',
                'managed': True,
            },
        ),
    ]
