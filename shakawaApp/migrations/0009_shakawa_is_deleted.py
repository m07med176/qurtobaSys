# Generated by Django 3.1.5 on 2021-12-08 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shakawaApp', '0008_auto_20211207_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='shakawa',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='تم مسحه'),
        ),
    ]
