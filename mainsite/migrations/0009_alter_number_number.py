# Generated by Django 4.2.2 on 2023-06-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainsite", "0008_alter_history_数字_alter_winners_数字"),
    ]

    operations = [
        migrations.AlterField(
            model_name="number",
            name="number",
            field=models.FloatField(),
        ),
    ]
