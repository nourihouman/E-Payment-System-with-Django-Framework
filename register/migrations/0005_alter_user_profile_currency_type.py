# Generated by Django 4.1.7 on 2023-04-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_alter_user_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='Currency_type',
            field=models.CharField(choices=[('GBP', 'UK Pounds'), ('USD', 'US Dollars'), ('EUR', 'EUro')], default='GBP', max_length=10),
        ),
    ]
