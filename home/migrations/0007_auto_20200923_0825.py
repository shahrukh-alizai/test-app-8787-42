# Generated by Django 2.2.16 on 2020-09-23 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0006_auto_20200911_1353"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dewtextddfddf",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=150)),
                ("news", models.CharField(blank=True, max_length=256, null=True)),
                ("phone", models.BigIntegerField(blank=True, null=True)),
                ("book", models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="MewModelsdf",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=150)),
                ("news", models.CharField(blank=True, max_length=256, null=True)),
                ("phone", models.BigIntegerField(blank=True, null=True)),
                ("book", models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="homepage",
            name="demo",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="homepage_demo",
                to="home.CustomText",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="test",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="homepage_test",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
