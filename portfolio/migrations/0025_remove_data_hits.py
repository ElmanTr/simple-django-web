# Generated by Django 3.1.2 on 2020-11-22 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0024_auto_20201115_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='hits',
        ),
    ]