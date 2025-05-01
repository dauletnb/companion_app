from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class LearningPath(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class MicroLesson(models.Model):
    path = models.ForeignKey(LearningPath, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100)
    content = models.TextField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(MicroLesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    points = models.IntegerField(default=0)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title}"

    def complete(self):
        """Метод для завершения урока и начисления баллов."""
        if not self.completed:
            self.completed = True
            # Начисляем баллы: 1 балл за каждую минуту урока, минимум 5 баллов
            self.points = max(self.lesson.duration, 5)
            self.completed_at = timezone.now()
            self.save()