from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import File
from .serializers import FileSerializer


class UploadFileView(APIView):
    '''
    Загрузка файла
    '''
    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        '''Обработка POST запроса'''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {'error': 'error', },
            status=status.HTTP_400_BAD_REQUEST
        )


class FileView(APIView):
    '''
    Вывод всех файлов
    '''
    permission_classes = (AllowAny,)
    serializer_class = FileSerializer

    def get(self, request):
        files = File.objects.all().order_by('-pk')
        serializer = FileSerializer(files, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
