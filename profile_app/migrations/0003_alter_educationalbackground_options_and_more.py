# Generated by Django 5.0.3 on 2024-06-18 21:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profile_app", "0002_educationalbackground_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="educationalbackground",
            options={"ordering": ["rank"]},
        ),
        migrations.RemoveField(
            model_name="educationalbackground",
            name="user",
        ),
        migrations.RemoveField(
            model_name="historicaleducationalbackground",
            name="user",
        ),
        migrations.AddField(
            model_name="educationalbackground",
            name="rank",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="educationalbackground",
            name="user_details",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="academic_histories",
                to="profile_app.userdetails",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="historicaleducationalbackground",
            name="rank",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="historicaleducationalbackground",
            name="user_details",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="profile_app.userdetails",
            ),
        ),
    ]
