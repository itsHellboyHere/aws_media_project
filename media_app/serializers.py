from rest_framework import serializers
from .models import MediaFile

class UploadRequestSerializer(serializers.Serializer):
    filename = serializers.CharField()
    content_type = serializers.CharField()
    

class MediaFileCreateSerializer(serializers.ModelSerializer):
    raw_s3_key = serializers.CharField(write_only=True)

    class Meta:
        model = MediaFile
        fields = ["raw_s3_key", "original_filename"]

    def create(self, validated_data):
        raw_key = validated_data.pop("raw_s3_key")
        compressed_key = raw_key.replace("raw/", "compressed/", 1)

        return MediaFile.objects.create(
            original_filename=validated_data["original_filename"],
            s3_compressed_key=compressed_key,
        )

class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ["id", "original_filename", "s3_compressed_key", "created_at"]