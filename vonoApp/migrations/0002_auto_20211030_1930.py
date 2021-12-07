# Generated by Django 3.1.5 on 2021-10-30 17:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vonoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vodafonenumber',
            options={'ordering': ['-updated_at'], 'verbose_name': 'رقم فودافون', 'verbose_name_plural': 'أرقام فودافون'},
        ),
        migrations.AddField(
            model_name='vodafonenumber',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vodafonenumber',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='vodafonenumber',
            name='version',
            field=models.DateField(default=django.utils.timezone.now, null=True, verbose_name='اخر إصدار'),
        ),
    ]