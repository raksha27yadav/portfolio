# Generated by Django 2.1.5 on 2021-01-02 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0007_updateaboutphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='updateaboutphoto',
            name='desc4',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
