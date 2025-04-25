from django.contrib import admin
from .models import LearningPath, MicroLesson, UserProgress

admin.site.register(LearningPath)
admin.site.register(MicroLesson)
admin.site.register(UserProgress)