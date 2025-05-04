from django.db import models


class Video(models.Model):
    file = models.FileField(upload_to='videos/')
    processed = models.BooleanField(default=False)
    result = models.JSONField(null=True, blank=True)
    output = models.FileField(upload_to='outputs/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
