# Generated by Django 3.2 on 2021-05-01 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210429_1427'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='guideversion',
            name='unique_guideversion',
        ),
        migrations.AddConstraint(
            model_name='guideversion',
            constraint=models.UniqueConstraint(fields=('guide_unique', 'name'), name='unique_guide_version'),
        ),
    ]
