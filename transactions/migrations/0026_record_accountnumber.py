# Generated by Django 3.1.5 on 2022-03-19 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0025_auto_20211225_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='accountNumber',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='رقم الحساب'),
        ),
    ]