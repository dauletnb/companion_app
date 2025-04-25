from rest_framework import serializers
from .models import LearningPath, MicroLesson, UserProgress

class LearningPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningPath
        fields = ['id', 'title', 'description', 'created_at']

class MicroLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroLesson
        fields = ['id', 'path', 'title', 'content', 'duration', 'created_at']

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = ['id', 'user', 'lesson', 'completed', 'points', 'completed_at']