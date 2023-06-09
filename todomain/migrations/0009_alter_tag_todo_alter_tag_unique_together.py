# Generated by Django 4.2 on 2023-04-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todomain", "0008_alter_tag_todo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="todo",
            field=models.ManyToManyField(
                blank=True, related_name="tag", to="todomain.todo"
            ),
        ),
        migrations.AlterUniqueTogether(name="tag", unique_together={("name",)},),
    ]
