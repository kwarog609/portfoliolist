# Generated by Django 4.2.10 on 2024-02-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("codingnotes", "0003_alter_notes_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notes",
            name="tags",
            field=models.ManyToManyField(
                related_name="tags", to="codingnotes.contenttag"
            ),
        ),
    ]
