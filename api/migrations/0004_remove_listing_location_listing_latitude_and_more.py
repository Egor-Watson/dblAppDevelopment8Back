# Generated by Django 4.0.2 on 2022-03-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_extrauserinformation_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='location',
        ),
        migrations.AddField(
            model_name='listing',
            name='latitude',
            field=models.CharField(default='0', max_length=7),
        ),
        migrations.AddField(
            model_name='listing',
            name='longitude',
            field=models.CharField(default='0', max_length=7),
        ),
    ]
