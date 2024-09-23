# Generated by Django 5.0.3 on 2024-06-30 05:55

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
            name="HistoricalTrainingWorkshop",
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
                ("name", models.CharField(max_length=255)),
                ("organizer", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("start_date", models.DateField()),
                ("completion_date", models.DateField(blank=True, null=True)),
                ("certificate", models.TextField()),
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
                "verbose_name": "historical training workshop",
                "verbose_name_plural": "historical training workshops",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="TrainingWorkshop",
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
                ("name", models.CharField(max_length=255)),
                ("organizer", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("start_date", models.DateField()),
                ("completion_date", models.DateField(blank=True, null=True)),
                ("certificate", models.TextField()),
                (
                    "user_details",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="training_workshops",
                        to="profile_app.userdetails",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
