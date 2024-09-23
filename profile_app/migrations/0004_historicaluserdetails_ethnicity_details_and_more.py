# Generated by Django 5.0.3 on 2024-06-26 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "profile_app",
            "0003_alter_historicaluserdetails_current_state_province_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="historicaluserdetails",
            name="ethnicity_details",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="historicaluserdetails",
            name="ethnicity_origin",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="historicaluserdetails",
            name="ethnicity_reporting",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="userdetails",
            name="ethnicity_details",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="userdetails",
            name="ethnicity_origin",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="userdetails",
            name="ethnicity_reporting",
            field=models.BooleanField(default=False),
        ),
    ]
