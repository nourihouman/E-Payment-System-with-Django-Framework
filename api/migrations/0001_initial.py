# Generated by Django 4.1.7 on 2023-03-30 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='convert_currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_currency', models.CharField(max_length=10)),
                ('to_currency', models.CharField(max_length=10)),
            ],
        ),
    ]
