# Generated by Django 4.2.6 on 2023-11-03 02:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doucecravingsnew_app", "0007_alter_list_of_items_date_modified"),
    ]

    operations = [
        migrations.AlterField(
            model_name="list_of_items",
            name="date_modified",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 3, 2, 18, 18, 617247)
            ),
        ),
        migrations.AlterField(
            model_name="list_of_items",
            name="toppings",
            field=models.CharField(default="funfetti,brownie crumbles"),
        ),
    ]