# Generated by Django 4.1.7 on 2023-04-17 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0009_notification_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcation',
            name='reference',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='request',
            name='reference',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='request',
            name='transfer_status',
            field=models.CharField(choices=[('successful', 'successful'), ('pending', 'Pending'), ('cancelled', 'Cancelled')], default='pending', max_length=10),
        ),
    ]