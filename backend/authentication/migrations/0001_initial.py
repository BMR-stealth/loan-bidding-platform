# Generated by Django 4.2.7 on 2024-12-08 00:51

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('LOAN_OFFICER', 'Loan Officer'), ('ADMIN', 'Admin')], max_length=20)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='LoanOfficerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmls_id', models.CharField(help_text='Loan officer NMLS ID', max_length=50, unique=True)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('subscription_plan', models.CharField(choices=[('BASIC', 'Basic'), ('PREMIUM', 'Premium'), ('ENTERPRISE', 'Enterprise')], default='BASIC', max_length=20)),
                ('total_loans_funded', models.IntegerField(default=0)),
                ('success_rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('license_expiry', models.DateField(blank=True, null=True)),
                ('years_of_experience', models.IntegerField(default=0)),
                ('specialties', models.JSONField(blank=True, default=list)),
                ('service_areas', models.JSONField(blank=True, default=list)),
                ('bio', models.TextField(blank=True)),
                ('profile_image', models.URLField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='loan_officer_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Loan Officer Profile',
                'verbose_name_plural': 'Loan Officer Profiles',
                'indexes': [models.Index(fields=['nmls_id'], name='authenticat_nmls_id_7bf232_idx'), models.Index(fields=['subscription_plan'], name='authenticat_subscri_cbc5ac_idx'), models.Index(fields=['is_active'], name='authenticat_is_acti_afbbd0_idx')],
            },
        ),
        migrations.AddIndex(
            model_name='customuser',
            index=models.Index(fields=['email'], name='authenticat_email_486e08_idx'),
        ),
        migrations.AddIndex(
            model_name='customuser',
            index=models.Index(fields=['role'], name='authenticat_role_cbb733_idx'),
        ),
    ]
