from celery import shared_task

from .models import File


@shared_task
def process_uploaded_file():
    '''
    Выполнение задачи celery (обработка файла)
    '''
    File.objects.filter(processed=False).update(processed=True)
