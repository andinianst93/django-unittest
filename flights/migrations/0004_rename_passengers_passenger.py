# Generated by Django 4.2.5 on 2023-09-24 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passengers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Passengers',
            new_name='Passenger',
        ),
    ]
