# Generated by Django 2.1.2 on 2018-12-06 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-created_time']},
        ),
    ]
