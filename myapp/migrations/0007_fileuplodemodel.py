# Generated by Django 4.2.5 on 2023-09-27 06:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0006_delete_person"),
    ]

    operations = [
        migrations.CreateModel(
            name="FileUplodeModel",
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
                ("images", models.ImageField(upload_to=None)),
                ("files", models.FileField(upload_to=None)),
            ],
        ),
    ]