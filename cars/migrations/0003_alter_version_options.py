# Generated by Django 5.0.6 on 2024-06-15 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0002_version"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="version",
            options={"verbose_name": "Версия", "verbose_name_plural": "Версии"},
        ),
    ]
