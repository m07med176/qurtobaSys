# Generated by Django 3.1.5 on 2021-12-22 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0011_auto_20211222_1443'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='إسم الحساب')),
                ('serial', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='رقم السيريال')),
                ('account', models.IntegerField(blank=True, null=True, verbose_name='رقم الحساب')),
                ('type', models.IntegerField(blank=True, choices=[(1, 'فورى'), (2, 'كاش'), (3, 'طاير'), (4, 'بى'), (5, 'أمان')], null=True, verbose_name='نوع الحساب')),
                ('sanf', models.IntegerField(blank=True, choices=[(1, '520 Contact كسر'), (2, '520 Contact زيرو بدون بطارية'), (3, '520 Contact كسر بدون بطارية'), (5, '520 Contact زيرو'), (6, '520 C كسر'), (7, 'nexgo نكس جو'), (8, 'موبايل كاش'), (9, 'موبايل فورى')], null=True, verbose_name='نوع الصنف')),
                ('stage', models.IntegerField(blank=True, choices=[(1, 'new machine'), (2, 'created'), (3, 'portal'), (4, 'validate'), (5, 'working')], default=1, null=True, verbose_name='نوع المخزن')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='السعر')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='التاريخ')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name='الوقت')),
                ('notes', models.TextField(blank=True, max_length=150, null=True, verbose_name='الملاحظات')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Store.customer+', to='customers.customerinfo', verbose_name='تابع لحساب')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Store.user+', to=settings.AUTH_USER_MODEL, verbose_name='المحاسب')),
            ],
            options={
                'verbose_name': 'إدارة الحسابات والمخازن',
                'verbose_name_plural': 'حساب',
                'managed': True,
            },
        ),
    ]
