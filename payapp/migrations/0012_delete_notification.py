# Generated by Django 4.1.7 on 2023-04-26 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0011_remove_transcation_transfer_status_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
