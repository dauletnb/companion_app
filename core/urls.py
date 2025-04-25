from django.urls import path
from .views import LearningPathList, MicroLessonList, UserProgressList

urlpatterns = [
    path('paths/', LearningPathList.as_view(), name='learning-path-list'),
    path('lessons/', MicroLessonList.as_view(), name='micro-lesson-list'),
    path('progress/', UserProgressList.as_view(), name='user-progress-list'),
]