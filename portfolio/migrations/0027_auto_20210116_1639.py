# Generated by Django 3.1.2 on 2021-01-16 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0026_auto_20201122_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='paragraph',
            new_name='paragraph_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='title',
        ),
        migrations.RemoveField(
            model_name='data',
            name='title',
        ),
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(default='', max_length=100, verbose_name='عنوان دسته بندی'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_fa',
            field=models.CharField(default='', max_length=100, verbose_name='عنوان دسته بندی'),
        ),
        migrations.AddField(
            model_name='data',
            name='paragraph_fa',
            field=models.TextField(default='', verbose_name='محتوا مقاله'),
        ),
        migrations.AddField(
            model_name='data',
            name='title_en',
            field=models.CharField(default='', max_length=100, verbose_name='عنوان مقاله'),
        ),
        migrations.AddField(
            model_name='data',
            name='title_fa',
            field=models.CharField(default='', max_length=100, verbose_name='عنوان مقاله'),
        ),
    ]
