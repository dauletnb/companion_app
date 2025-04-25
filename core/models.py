from django.db import models
from django.contrib.auth.models import User

class LearningPath(models.Model):
    title = models.CharField(max_length=100)  # Название пути, например, "Путь стоика"
    description = models.TextField()  # Описание пути
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return self.title

class MicroLesson(models.Model):
    path = models.ForeignKey(LearningPath, on_delete=models.CASCADE, related_name='lessons')  # Связь с путем
    title = models.CharField(max_length=100)  # Заголовок урока
    content = models.TextField()  # Содержание урока
    duration = models.IntegerField()  # Длительность в минутах
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    lesson = models.ForeignKey(MicroLesson, on_delete=models.CASCADE)  # Связь с уроком
    completed = models.BooleanField(default=False)  # Завершен ли урок
    points = models.IntegerField(default=0)  # Баллы за урок
    completed_at = models.DateTimeField(null=True, blank=True)  # Дата завершения

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title}"