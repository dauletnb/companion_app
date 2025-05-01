from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from django.utils import timezone
from django.db import models
from .models import LearningPath, MicroLesson, UserProgress
from .serializers import LearningPathSerializer, MicroLessonSerializer, UserProgressSerializer

class LearningPathViewSet(viewsets.ModelViewSet):
    queryset = LearningPath.objects.prefetch_related('lessons')
    serializer_class = LearningPathSerializer

class MicroLessonViewSet(viewsets.ModelViewSet):
    queryset = MicroLesson.objects.all()
    serializer_class = MicroLessonSerializer

class UserProgressViewSet(viewsets.ModelViewSet):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.completed and instance.points == 0:
            instance.complete()

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "This endpoint is for user registration. Send a POST request with username, password, and email."}, status=status.HTTP_200_OK)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        if not username or not password or not email:
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({'message': 'User created'}, status=status.HTTP_201_CREATED)

class UserPointsView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        total_points = UserProgress.objects.filter(user=request.user).aggregate(total_points=models.Sum('points'))['total_points'] or 0
        return Response({'total_points': total_points}, status=status.HTTP_200_OK)