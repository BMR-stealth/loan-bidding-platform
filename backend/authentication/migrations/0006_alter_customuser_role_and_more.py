# Generated by Django 4.2.7 on 2024-12-08 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_loanofficerpreferences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('LOAN_OFFICER', 'Loan Officer'), ('BORROWER', 'Borrower')], max_length=20),
        ),
        migrations.AlterField(
            model_name='loanofficerprofile',
            name='subscription_plan',
            field=models.CharField(choices=[('FREE', 'Free'), ('BASIC', 'Basic'), ('PREMIUM', 'Premium')], default='BASIC', max_length=20),
        ),
    ]
