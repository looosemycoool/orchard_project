# Generated by Django 4.2.2 on 2023-07-29 06:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reserve", "0007_alter_reserve_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reserve",
            name="content",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]