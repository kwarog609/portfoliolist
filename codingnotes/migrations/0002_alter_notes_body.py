# Generated by Django 4.2.10 on 2024-02-18 12:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("codingnotes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notes", name="body", field=ckeditor.fields.RichTextField(),
        ),
    ]