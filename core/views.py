from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
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


class CompleteLessonView(APIView):
    def post(self, request, lesson_id):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            lesson = MicroLesson.objects.get(id=lesson_id)
        except MicroLesson.DoesNotExist:
            return Response({"error": "Lesson not found"}, status=status.HTTP_404_NOT_FOUND)

        progress, created = UserProgress.objects.get_or_create(
            user=request.user,
            lesson=lesson,
            defaults={'completed': False, 'points': 0}
        )
        progress.complete()
        return Response({
            "message": "Lesson completed",
            "points": progress.points,
            "completed": progress.completed
        }, status=status.HTTP_200_OK)