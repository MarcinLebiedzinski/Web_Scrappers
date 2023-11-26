import pickle
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_scrappers.settings')

app = Celery('web_scrappers')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.task_routes = {'ikea_outlet.tasks.get_all_articles': {'queue':'queue1'}, 
                        'ikea_outlet.tasks.scrap': {'queue':'queue1'}}

app.conf.task_serializer = 'pickle'
app.conf.result_serializer = 'pickle'
app.conf.event_serializer = 'pickle'
app.conf.accept_content = ['pickle']
app.conf.task_accept_content = ['pickle']
app.conf.result_accept_content = ['pickle']
app.conf.event_accept_content = ['pickle']


app.autodiscover_tasks()



