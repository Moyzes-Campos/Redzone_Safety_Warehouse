from django.contrib import admin
from .models import Video
from .tasks import process_video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'processed', 'created_at')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # dispara o processamento se for um upload novo (não somente edição)
        if not change:
            process_video.delay(obj.id)
