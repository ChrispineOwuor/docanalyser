from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    filename = serializers.FileField(required=True)
