# Generated by Django 4.2 on 2023-04-16 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tags", "0003_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="taggeditem", name="content_type",),
        migrations.RemoveField(model_name="taggeditem", name="tag",),
        migrations.DeleteModel(name="Tag",),
        migrations.DeleteModel(name="TaggedItem",),
    ]