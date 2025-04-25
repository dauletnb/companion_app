from rest_framework import generics
from .models import LearningPath, MicroLesson, UserProgress
from .serializers import LearningPathSerializer, MicroLessonSerializer, UserProgressSerializer

class LearningPathList(generics.ListCreateAPIView):
    queryset = LearningPath.objects.all()
    serializer_class = LearningPathSerializer

class MicroLessonList(generics.ListCreateAPIView):
    queryset = MicroLesson.objects.all()
    serializer_class = MicroLessonSerializer

class UserProgressList(generics.ListCreateAPIView):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer