# Generated by Django 4.0.2 on 2022-03-28 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_alter_listing_latitude_alter_listing_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_made', models.DateField(auto_created=True)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('D', 'Declined')], max_length=1)),
                ('offer_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offerFor_listing', to='api.listing')),
                ('offering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.listing')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
