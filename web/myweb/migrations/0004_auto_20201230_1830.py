# Generated by Django 2.1.5 on 2020-12-30 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0003_updatecertifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateCertiPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='myweb/images')),
            ],
        ),
        migrations.RemoveField(
            model_name='updatecertifications',
            name='image',
        ),
    ]