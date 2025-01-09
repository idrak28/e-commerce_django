# Generated by Django 5.1.4 on 2025-01-08 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_remove_book_store_name_bookstore_book_list"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookstore",
            name="book_list",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="book_list",
                to="api.book",
            ),
        ),
    ]
