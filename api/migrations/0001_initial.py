# Generated by Django 3.0.5 on 2021-04-27 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='наименование')),
                ('slug', models.SlugField(verbose_name='короткое наименование')),
                ('description', models.TextField(null=True, verbose_name='описание')),
                ('start_date', models.DateField(verbose_name='дата начала действия')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='GuideVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='версия справочника')),
                ('guide_unique', models.CharField(blank=True, max_length=32, null=True, verbose_name='идентификатор справочника')),
                ('date_from', models.DateField(verbose_name='дата начала действия')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='api.Guide', verbose_name='наименование справочника')),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='код')),
                ('value', models.CharField(max_length=200, verbose_name='значение')),
                ('version', models.ManyToManyField(blank=True, related_name='elements', to='api.GuideVersion', verbose_name='версия справочника')),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.AddConstraint(
            model_name='guideversion',
            constraint=models.UniqueConstraint(fields=('guide_unique', 'name'), name='unique guideversion'),
        ),
    ]