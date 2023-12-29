# Generated by Django 4.2.2 on 2023-12-28 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("check", "0011_remove_breakuser_break_time_remove_breakuser_user_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Patrol_Check",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(null=True)),
                ("day_of_week", models.CharField(blank=True, max_length=3, null=True)),
                (
                    "time1_study",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time1_focus",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time2_study",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time2_focus",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time3_study",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time3_focus",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time4_study",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time4_focus",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time5_study",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time5_focus",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time6_study",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time6_focus",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time7_study",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time7_focus",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time8_study",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time8_focus",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time9_study",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time9_focus",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time10_study",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time10_focus",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time11_study",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time11_focus",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time12_study",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time12_focus",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time13_study",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time13_focus",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time14_study",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time14_focus",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time15_study",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time15_focus",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time16_study",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time16_focus",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time17_study",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time17_focus",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time18_study",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time18_focus",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="check.studentregister",
                    ),
                ),
            ],
        ),
    ]
