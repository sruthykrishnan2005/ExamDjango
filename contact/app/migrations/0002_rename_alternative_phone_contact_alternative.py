# Generated by Django 5.1.3 on 2025-01-14 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='alternative_phone',
            new_name='alternative',
        ),
    ]
