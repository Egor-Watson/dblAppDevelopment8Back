# Generated by Django 4.0.2 on 2022-03-16 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_extrauserinformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image1',
            field=models.TextField(blank=True, max_length=65000, null=True),
        ),
    ]
