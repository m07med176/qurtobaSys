# Generated by Django 3.1.5 on 2022-02-27 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vcashApp', '0006_sim'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(blank=True, null=True)),
                ('dateinsert', models.DateField(blank=True, null=True)),
                ('timeinsert', models.TimeField(blank=True, null=True)),
                ('datetimeinsert', models.DateTimeField(blank=True, null=True)),
                ('dateremove', models.DateField(blank=True, null=True)),
                ('timeremove', models.TimeField(blank=True, null=True)),
                ('datetimeremove', models.DateTimeField(blank=True, null=True)),
                ('sim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vcashApp.sim')),
            ],
            options={
                'managed': True,
            },
        ),
    ]