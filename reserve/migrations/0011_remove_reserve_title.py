# Generated by Django 4.2.2 on 2024-01-08 16:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("reserve", "0010_reserve_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reserve",
            name="title",
        ),
    ]
