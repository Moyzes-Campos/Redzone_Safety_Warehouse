from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import VideoViewSet

router = DefaultRouter()
router.register('videos', VideoViewSet, basename='video')

urlpatterns = [
    path('', include(router.urls)),
]