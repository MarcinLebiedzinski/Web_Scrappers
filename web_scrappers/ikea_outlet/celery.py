import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_scrappers.settings')

app = Celery('ikea_outlet')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
