# Generated by Django 4.2 on 2023-04-16 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todomain", "0003_tag_taggeditem"),
    ]

    operations = [
        migrations.RemoveField(model_name="taggeditem", name="tag",),
        migrations.DeleteModel(name="Tag",),
        migrations.DeleteModel(name="TaggedItem",),
    ]
