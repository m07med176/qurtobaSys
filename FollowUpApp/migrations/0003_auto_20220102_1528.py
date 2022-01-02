# Generated by Django 3.1.5 on 2022-01-02 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FollowUpApp', '0002_auto_20211230_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FollowUp.user+', to='FollowUpApp.employers', verbose_name='الموظف'),
        ),
    ]
