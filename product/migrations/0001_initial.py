# Generated by Django 4.2.1 on 2023-06-04 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100)),
                ("price", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="PlaceOrder",
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
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("item_amount", models.PositiveIntegerField(default=1)),
                ("total_cost", models.PositiveIntegerField()),
                ("full_name", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=100)),
                ("delivery_address", models.CharField(max_length=100)),
                ("is_verified", models.BooleanField(default=False)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.expressions.Case,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
