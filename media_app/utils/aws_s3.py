# media_app/utils/aws_s3.py
import boto3
from django.conf import settings

def get_s3_client():
    return boto3.client(
        "s3",
        region_name=settings.AWS_REGION,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )

def create_presigned_upload_url(key: str, content_type: str, expires_in: int = 3600):
    s3_client = get_s3_client()
    return s3_client.generate_presigned_url(
        "put_object",
        Params={
            "Bucket": settings.AWS_STORAGE_BUCKET_NAME,
            "Key": key,
            "ContentType": content_type,
        },
        ExpiresIn=expires_in,
    )

def create_presigned_get_url(key: str, expires_in: int = 3600):
    s3_client = get_s3_client()
    return s3_client.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": settings.AWS_STORAGE_BUCKET_NAME,
            "Key": key,
        },
        ExpiresIn=expires_in,
    )