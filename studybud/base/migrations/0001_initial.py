# Generated by Django 4.2.4 on 2023-08-27 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Room",
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
                ("name", models.CharField(max_length=256)),
                ("description", models.TextField(blank=True, null=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]