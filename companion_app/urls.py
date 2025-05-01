from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import LearningPathViewSet, MicroLessonViewSet, UserProgressViewSet, RegisterView, UserPointsView

router = DefaultRouter()
router.register(r'paths', LearningPathViewSet)
router.register(r'lessons', MicroLessonViewSet)
router.register(r'progress', UserProgressViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/points/', UserPointsView.as_view(), name='user-points'),
]