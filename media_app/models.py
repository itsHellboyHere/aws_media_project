from django.db import models

class MediaFile(models.Model):
    original_filename = models.CharField(max_length=255)
    s3_compressed_key = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_filename