# Generated by Django 3.1.5 on 2021-10-22 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transactions', '0002_auto_20211022_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='accountant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='accountant', to=settings.AUTH_USER_MODEL, verbose_name='المحاسب'),
        ),
    ]
