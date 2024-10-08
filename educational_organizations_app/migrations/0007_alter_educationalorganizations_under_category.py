# Generated by Django 5.0.3 on 2024-07-30 20:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "educational_organizations_app",
            "0006_educationalorganizations_created_by_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="educationalorganizations",
            name="under_category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="educational_organizations_app.educationalorganizationscategory",
                verbose_name="Category",
            ),
        ),
    ]