# Generated by Django 2.1.5 on 2021-01-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0006_updateskills'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateAboutphoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='', upload_to='myweb/images')),
            ],
        ),
    ]
