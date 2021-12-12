# Generated by Django 3.1.5 on 2021-12-12 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0017_auto_20211031_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='type',
            field=models.CharField(choices=[('فورى', 'فورى'), ('كاش', 'كاش'), ('طاير', 'طاير'), ('بى', 'بى'), ('أمان', 'أمان'), ('أخرى', 'أخرى'), ('تنزيل', 'تنزيل'), ('تحصيل', 'تحصيل'), ('شراء', 'شراء')], default=1, max_length=50, verbose_name='نوع الحساب'),
        ),
    ]
