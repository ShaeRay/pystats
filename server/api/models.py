from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)