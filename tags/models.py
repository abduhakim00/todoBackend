from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'tags'


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tags')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='tag')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


    class Meta:
        db_table = 'taggedItems'