# Generated by Django 5.0.3 on 2024-07-08 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0008_merge_20240628_0353"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicaluserdocument",
            name="use",
            field=models.CharField(
                choices=[
                    ("resume", "Resume"),
                    ("sop", "SOP"),
                    ("image", "Image"),
                    ("organization_logo", "Image"),
                    ("birth_certificate", "Birth Certificate"),
                    ("passport", "Passport"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="userdocument",
            name="use",
            field=models.CharField(
                choices=[
                    ("resume", "Resume"),
                    ("sop", "SOP"),
                    ("image", "Image"),
                    ("organization_logo", "Image"),
                    ("birth_certificate", "Birth Certificate"),
                    ("passport", "Passport"),
                ],
                max_length=20,
            ),
        ),
    ]
