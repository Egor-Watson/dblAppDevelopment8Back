# Generated by Django 4.0.2 on 2022-03-28 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_listing_archived_listing_featured_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='date_made',
            field=models.DateField(auto_now_add=True),
        ),
    ]
