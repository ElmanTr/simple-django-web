# Generated by Django 3.1.1 on 2020-10-23 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_auto_20201022_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='status',
            field=models.CharField(choices=[('d', 'پیش نویس'), ('p', 'منتشر شده'), ('i', 'در حال بررسی')], default='d', max_length=1, verbose_name='وضعیت'),
        ),
    ]
