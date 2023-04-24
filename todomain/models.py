from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    PRIORITY_HIGH = 'P1'
    PRIORITY_MID = 'P2'
    PRIORITY_LOW = 'P3'

    PRIORITIES = [
        (PRIORITY_HIGH, "Urgent"),
        (PRIORITY_MID, 'Important'),
        (PRIORITY_LOW, 'Secondary')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=2, choices=PRIORITIES, default=PRIORITY_LOW)
    due_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'todos'

class Tag(models.Model):
    name = models.CharField(max_length=255)
    todo = models.ManyToManyField(Todo, related_name='tag', blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        unique_together = [['name']]


# class TaggedItem(models.Model):
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='todo')

#     def __str__(self) -> str:
#         return self.tag.name
