# Generated by Django 3.1.5 on 2021-10-22 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='type',
            field=models.CharField(choices=[('فورى', 'فورى'), ('كاش', 'كاش'), ('طاير', 'طاير'), ('بى', 'بى'), ('أمان', 'أمان'), ('أخرى', 'أخرى'), ('تنزيل', 'تنزيل'), ('تحصيل', 'تحصيل')], default=1, max_length=50, verbose_name='نوع الحساب'),
        ),
    ]
