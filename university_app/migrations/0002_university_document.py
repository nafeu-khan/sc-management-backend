# Generated by Django 5.0.3 on 2024-03-23 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("university_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="university",
            name="document",
            field=models.FileField(
                blank=True, null=True, upload_to="university_documents/"
            ),
        ),
    ]
