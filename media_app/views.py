import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import UploadRequestSerializer
from .utils.aws_s3 import create_presigned_upload_url,create_presigned_get_url
from .models import MediaFile
from .serializers import MediaFileCreateSerializer,MediaFileSerializer


from django.conf import settings

class GenerateUploadURLView(APIView):
    def post(self,request):
        serializer = UploadRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        filename = serializer.validated_data["filename"]
        content_type=serializer.validated_data["content_type"]

        # generate unique key in raw/ folder

        ext = filename.split(".")[-1]
        unique_id=uuid.uuid4().hex
        s3_key = f"raw/{unique_id}.{ext}"

        upload_url= create_presigned_upload_url(
            key=s3_key,
            content_type=content_type,
        )
        return Response(
            {
                "upload_url": upload_url,
                "raw_key": s3_key, 
            },
            status=status.HTTP_200_OK,
        )

class MediaFileCreateView(generics.CreateAPIView):
    serializer_class= MediaFileCreateSerializer

class MediaFileListView(generics.ListAPIView):
    queryset= MediaFile.objects.all().order_by('-created_at')
    serializer_class= MediaFileSerializer

    def list(self,request,*args,**kwargs):
        response = super().list(request,*args, **kwargs)
        
        for item in response.data:
            print(item)
            key = item["s3_compressed_key"]
            item["file_url"] = create_presigned_get_url(key)
        return response
    