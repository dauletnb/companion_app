from rest_framework import serializers
from .models import LearningPath, MicroLesson, UserProgress

class MicroLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroLesson
        fields = ['id', 'path', 'title', 'content', 'duration', 'created_at']

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = ['id', 'user', 'lesson', 'completed', 'points', 'completed_at']

class LearningPathSerializer(serializers.ModelSerializer):
    lessons = MicroLessonSerializer(many=True, read_only=True)
    completion_percentage = serializers.SerializerMethodField()

    class Meta:
        model = LearningPath
        fields = ['id', 'title', 'description', 'created_at', 'lessons', 'completion_percentage']

    def get_completion_percentage(self, obj):
        user = self.context['request'].user
        if not user.is_authenticated:
            return 0
        lessons = obj.lessons.all()
        total_lessons = lessons.count()
        if total_lessons == 0:
            return 0
        completed_lessons = UserProgress.objects.filter(
            user=user, lesson__path=obj, completed=True
        ).count()
        percentage = (completed_lessons / total_lessons) * 100
        return round(percentage, 2)  # Округляем до 2 знаков после запятой