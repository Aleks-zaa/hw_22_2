# Generated by Django 5.0.6 on 2024-06-15 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0005_alter_version_car_alter_version_number"),
    ]

    operations = [
        migrations.RenameField(
            model_name="version",
            old_name="car",
            new_name="vers",
        ),
    ]
