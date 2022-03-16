# Generated by Django 4.0.2 on 2022-03-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_listing_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='image',
        ),
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.CharField(default='category', max_length=30),
        ),
        migrations.AddField(
            model_name='listing',
            name='image1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='image2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='image3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='image4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='location',
            field=models.CharField(default='location', max_length=30),
        ),
        migrations.AddField(
            model_name='listing',
            name='similar_items',
            field=models.TextField(default='item', max_length=300),
        ),
        migrations.AlterField(
            model_name='listing',
            name='offers',
            field=models.ManyToManyField(blank=True, null=True, to='api.Listing'),
        ),
        migrations.DeleteModel(
            name='Offer',
        ),
    ]