# Generated by Django 4.2.7 on 2024-12-09 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_loanofficerprofile_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanofficerprofile',
            name='active_bids_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='loanofficerprofile',
            name='total_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='loanofficerprofile',
            name='success_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
