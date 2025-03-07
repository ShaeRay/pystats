from rest_framework import serializers
from .models import UploadedFile

class UploadedFileSerializer(serializers.ModelSerializer):
    data = serializers.JSONField()

    class Meta:
        model = UploadedFile
        fields = ('file', 'data')