# Generated by Django 4.2.2 on 2023-06-19 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_location_lat_remove_location_lng'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='lat',
            field=models.DecimalField(decimal_places=5, default=20.98813, max_digits=7),
        ),
        migrations.AddField(
            model_name='location',
            name='lng',
            field=models.DecimalField(decimal_places=5, default=47.62217, max_digits=7),
        ),
    ]
