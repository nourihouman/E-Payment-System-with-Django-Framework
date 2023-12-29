# Generated by Django 4.1.7 on 2023-04-22 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_convert_currency_converting_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='converting_currency',
            name='rate',
            field=models.DecimalField(decimal_places=3, default='1', max_digits=8),
        ),
    ]
