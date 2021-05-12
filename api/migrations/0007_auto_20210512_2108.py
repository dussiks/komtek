# Generated by Django 3.2 on 2021-05-12 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210501_1454'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guideversion',
            options={'get_latest_by': 'date_from'},
        ),
        migrations.AlterField(
            model_name='element',
            name='code',
            field=models.CharField(max_length=50, unique=True, verbose_name='код'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=30, unique=True, verbose_name='короткое наименование'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='наименование справочника'),
        ),
    ]