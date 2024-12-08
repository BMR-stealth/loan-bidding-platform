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
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('credit_score', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(300), django.core.validators.MaxValueValidator(850)])),
                ('annual_income', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('employment_status', models.CharField(blank=True, max_length=50)),
                ('property_type', models.CharField(blank=True, max_length=50)),
                ('property_use', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Borrower',
                'verbose_name_plural': 'Borrowers',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('original_apr', models.DecimalField(decimal_places=2, default=5.0, max_digits=5)),
                ('location', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('NEW', 'New'), ('AVAILABLE', 'Available'), ('IN_PROGRESS', 'In Progress'), ('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('CLOSED', 'Closed'), ('EXPIRED', 'Expired')], default='AVAILABLE', max_length=20)),
                ('fico_score', models.IntegerField(default=700, validators=[django.core.validators.MinValueValidator(300), django.core.validators.MaxValueValidator(850)])),
                ('lead_type', models.CharField(choices=[('GUARANTEED', 'Guaranteed'), ('COMPETITIVE', 'Competitive')], default='COMPETITIVE', max_length=20)),
                ('lowest_bid_apr', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('max_bids', models.IntegerField(default=10)),
                ('current_bid_count', models.IntegerField(default=0)),
                ('is_guaranteed', models.BooleanField(default=False)),
                ('is_closed', models.BooleanField(default=False)),
                ('loan_type', models.CharField(blank=True, max_length=50)),
                ('loan_term', models.IntegerField(blank=True, null=True)),
                ('property_value', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('down_payment', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('monthly_payment', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('debt_to_income_ratio', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('loan_estimate_document', models.URLField(blank=True)),
                ('additional_documents', models.JSONField(blank=True, default=list)),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='loans.borrower')),
                ('current_leader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leading_loans', to='authentication.loanofficerprofile')),
                ('winning_bid', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='won_loan', to='bidding.bid')),
            ],
            options={
                'verbose_name': 'Loan',
                'verbose_name_plural': 'Loans',
            },
        ),
        migrations.CreateModel(
            name='GuaranteedLeadAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_at', models.DateTimeField(auto_now_add=True)),
                ('loan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='guaranteed_assignment', to='loans.loan')),
                ('loan_officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guaranteed_leads', to='authentication.loanofficerprofile')),
            ],
            options={
                'verbose_name': 'Guaranteed Lead Assignment',
                'verbose_name_plural': 'Guaranteed Lead Assignments',
            },
        ),
        migrations.CreateModel(
            name='GuaranteedLeadAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credits_available', models.IntegerField(default=3)),
                ('credits_used', models.IntegerField(default=0)),
                ('reset_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('loan_officer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='guaranteed_allocation', to='authentication.loanofficerprofile')),
            ],
            options={
                'verbose_name': 'Guaranteed Lead Allocation',
                'verbose_name_plural': 'Guaranteed Lead Allocations',
            },
        ),
        migrations.AddIndex(
            model_name='borrower',
            index=models.Index(fields=['email'], name='loans_borro_email_b4520e_idx'),
        ),
        migrations.AddIndex(
            model_name='borrower',
            index=models.Index(fields=['credit_score'], name='loans_borro_credit__c28d38_idx'),
        ),
        migrations.AddIndex(
            model_name='borrower',
            index=models.Index(fields=['annual_income'], name='loans_borro_annual__aa2c2e_idx'),
        ),
        migrations.AddIndex(
            model_name='loan',
            index=models.Index(fields=['borrower'], name='loans_loan_borrowe_4ce53f_idx'),
        ),
        migrations.AddIndex(
            model_name='loan',
            index=models.Index(fields=['status'], name='loans_loan_status_962e99_idx'),
        ),
        migrations.AddIndex(
            model_name='loan',
            index=models.Index(fields=['lead_type'], name='loans_loan_lead_ty_a2eb70_idx'),
        ),
        migrations.AddIndex(
            model_name='loan',
            index=models.Index(fields=['created_at'], name='loans_loan_created_80fd62_idx'),
        ),
    ]
