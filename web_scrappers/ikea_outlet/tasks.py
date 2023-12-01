from .models import Market, Article
from web_scrappers.celery import app
from celery import shared_task
from datetime import timedelta

from utils.mail_functions import send_mail
from utils.scraping_functions import scrap

app.conf.beat_schedule = {
    'task1':{
        'task': 'ikea_outlet.tasks.test_beat',
        'schedule': timedelta(seconds=60),
    },
    'task2':{
        'task': 'ikea_outlet.tasks.scrap_beat',
        'schedule': timedelta(seconds=300),
    },
    'task3':{
        'task': 'ikea_outlet.tasks.send_mail_beat',
        'schedule': timedelta(seconds=600),
    },
}

@app.task(queue="queue1")
def test_beat():
    print("Just every 60 second test")
    return

@app.task(queue="queue1")
def scrap_beat():
    my_list = scrap()
    return len(my_list)


@app.task(queue="queue1")
def send_mail_beat():
    host = 'smtp.yandex.com'
    port = 465

    login = 'ikeabotalert'
    app_password = 'trudpsfzlcyghoes' # password generated in Yandex

    from_addr = 'ikeabotalert@yandex.com'
    to_addrs = 'lebiedzinski.marcin@gmail.com'
    message = """Subject: Your bot Ikea alert\n
    It's just test mail. It will contain sales in ikea outlet market in the nearest future
    """

    return send_mail(host, port, login, app_password, from_addr, to_addrs, message)