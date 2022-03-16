# Generated by Django 4.0.2 on 2022-02-18 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='listing',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='offering',
        ),
        migrations.AddField(
            model_name='listing',
            name='offers',
            field=models.ManyToManyField(to='api.Offer'),
        ),
        migrations.AddField(
            model_name='offer',
            name='item',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.listing'),
            preserve_default=False,
        ),
    ]