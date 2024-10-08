# Generated by Django 5.0.3 on 2024-07-25 05:12

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0012_alter_historicaluserdocument_use_and_more"),
        ("profile_app", "0011_alter_historicalreferenceinfo_title_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalTestScore",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("updated_at", models.DateTimeField(blank=True, editable=False)),
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                (
                    "test_name",
                    models.CharField(
                        choices=[
                            ("IELTS", "IELTS"),
                            ("TOEFL", "TOEFL"),
                            ("SAT", "SAT"),
                            ("GRE", "GRE"),
                            ("DUOLINGO", "DUOLINGO"),
                            ("PTE", "PTE"),
                        ],
                        max_length=100,
                    ),
                ),
                ("score", models.FloatField()),
                ("date_taken", models.DateField()),
                ("verified", models.BooleanField(default=False)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user_document",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="common.userdocument",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical test score",
                "verbose_name_plural": "historical test scores",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="TestScore",
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
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "test_name",
                    models.CharField(
                        choices=[
                            ("IELTS", "IELTS"),
                            ("TOEFL", "TOEFL"),
                            ("SAT", "SAT"),
                            ("GRE", "GRE"),
                            ("DUOLINGO", "DUOLINGO"),
                            ("PTE", "PTE"),
                        ],
                        max_length=100,
                    ),
                ),
                ("score", models.FloatField()),
                ("date_taken", models.DateField()),
                ("verified", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user_document",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="common.userdocument",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
