from rest_framework import serializers
from datetime import date
from . import models

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Todo
        fields=['id','title', 'description', 'priority', 'deadline', 'tag']

    # due_date = serializers.DateField(write_only=True)
    tag = serializers.StringRelatedField(many=True)    
    deadline = serializers.SerializerMethodField()
    def get_deadline(self, todo: models.Todo):
        today = date.today()
        if todo.due_date < today:
            return "obsolete"
        elif todo.due_date == today:
            return 'today'
        else:
            return todo.due_date


class TodoSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = models.Todo
        fields = ['id', 'title', 'description', 'priority', 'due_date','tag']
    
    def validate_tag(self, tags):
        for tag in tags:
            if not models.Tag.objects.filter(pk=tag.id).exists():
                raise serializers.ValidationError('No such a tag exists!')
        print(tags)
        return tags
    
    def create(self, validated_data):
        user_id = self.context['user_id']
        validated_data['user'] = user_id
        return super().create(validated_data)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ['id', 'name']