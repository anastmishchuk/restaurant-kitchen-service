# Generated by Django 5.0.2 on 2024-02-21 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cook",
            name="years_of_experience",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
