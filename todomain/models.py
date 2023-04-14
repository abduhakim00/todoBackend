from django.db import models

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

