# Generated by Django 2.1.5 on 2021-01-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0015_updatecolor'),
    ]

    operations = [
        migrations.AddField(
            model_name='updatecolor',
            name='svg',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='updatecolor',
            name='txt',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
