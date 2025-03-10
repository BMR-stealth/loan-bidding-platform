# Generated by Django 4.2.7 on 2024-12-08 00:51

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bidding', '0001_initial'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('SUBSCRIPTION', 'Subscription Payment'), ('BID_FEE', 'Competitive Bid Fee'), ('REFUND', 'Refund'), ('OTHER', 'Other')], max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed'), ('REFUNDED', 'Refunded')], default='PENDING', max_length=20)),
                ('description', models.CharField(max_length=255)),
                ('payment_method', models.CharField(blank=True, max_length=50)),
                ('payment_id', models.CharField(blank=True, max_length=100)),
                ('stripe_charge_id', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('bid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to='bidding.bid')),
                ('loan_officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='authentication.loanofficerprofile')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['loan_officer'], name='transaction_loan_of_f5a19d_idx'), models.Index(fields=['transaction_type'], name='transaction_transac_09d7ec_idx'), models.Index(fields=['status'], name='transaction_status_71abbb_idx'), models.Index(fields=['created_at'], name='transaction_created_67ce7b_idx')],
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('CANCELLED', 'Cancelled'), ('EXPIRED', 'Expired'), ('PENDING', 'Pending')], default='PENDING', max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('billing_cycle', models.CharField(default='MONTHLY', max_length=20)),
                ('stripe_subscription_id', models.CharField(blank=True, max_length=100)),
                ('stripe_customer_id', models.CharField(blank=True, max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cancelled_at', models.DateTimeField(blank=True, null=True)),
                ('loan_officer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='authentication.loanofficerprofile')),
            ],
            options={
                'verbose_name': 'Subscription',
                'verbose_name_plural': 'Subscriptions',
                'indexes': [models.Index(fields=['loan_officer'], name='transaction_loan_of_f1c35b_idx'), models.Index(fields=['status'], name='transaction_status_e51415_idx'), models.Index(fields=['end_date'], name='transaction_end_dat_eb6ee6_idx')],
            },
        ),
    ]
