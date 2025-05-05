from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from .tasks import process_video  # vamos criar em breve
from django.db import transaction


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('-created_at')
    serializer_class = VideoSerializer

    def perform_create(self, serializer):
        video = serializer.save()
        # Dispara processamento assíncrono
        transaction.on_commit(lambda: process_video.delay(video.id))
