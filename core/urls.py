from django.urls import path
from .views import LearningPathList, MicroLessonList, UserProgressList, CompleteLessonView

urlpatterns = [
    path('paths/', LearningPathList.as_view(), name='learning-path-list'),
    path('lessons/', MicroLessonList.as_view(), name='micro-lesson-list'),
    path('progress/', UserProgressList.as_view(), name='user-progress-list'),
    path('lessons/<int:lesson_id>/complete/', CompleteLessonView.as_view(), name='complete-lesson'),
]