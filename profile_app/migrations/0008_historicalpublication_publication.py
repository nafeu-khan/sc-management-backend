# Generated by Django 5.0.3 on 2024-06-28 04:03

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profile_app", "0007_merge_20240628_0009"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalPublication",
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
                ("title", models.CharField(max_length=255)),
                (
                    "publication_type",
                    models.CharField(
                        choices=[
                            ("journal", "Journal"),
                            ("workshop", "Workshop"),
                            ("conference", "Conference"),
                        ],
                        max_length=20,
                    ),
                ),
                ("authors", models.TextField()),
                ("publication_date", models.DateField()),
                ("abstract", models.TextField()),
                ("name", models.CharField(max_length=255)),
                ("doi_link", models.URLField(max_length=255)),
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
                    "user_details",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="profile_app.userdetails",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical publication",
                "verbose_name_plural": "historical publications",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="Publication",
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
                ("title", models.CharField(max_length=255)),
                (
                    "publication_type",
                    models.CharField(
                        choices=[
                            ("journal", "Journal"),
                            ("workshop", "Workshop"),
                            ("conference", "Conference"),
                        ],
                        max_length=20,
                    ),
                ),
                ("authors", models.TextField()),
                ("publication_date", models.DateField()),
                ("abstract", models.TextField()),
                ("name", models.CharField(max_length=255)),
                ("doi_link", models.URLField(max_length=255)),
                (
                    "user_details",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="publications",
                        to="profile_app.userdetails",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
