from .models import Market, Article, Search
from web_scrappers.celery import app
from celery import shared_task
from datetime import timedelta

from utils.functions import send_mail
from utils.functions import scrap, clear_db, save_result_to_db, search_phrase_in_results

app.conf.beat_schedule = {
    'task1':{
        'task': 'ikea_outlet.tasks.test_beat',
        'schedule': timedelta(seconds=60),
    },
    'task2':{
        'task': 'ikea_outlet.tasks.alert_beat',
        'schedule': timedelta(seconds=600),
    },
}

@app.task(queue="queue1")
def test_beat():
    print("Just every 60 second test")
    return

@app.task(queue="queue1")
def alert_beat():
    result_list = scrap()
    clear_db()
    save_result_to_db(result_list)
    search_list = Search.objects.all()
    for search in search_list:
        message_body = "Hello, This is ikea outlet alert.\n Below list of products that you interested in.\n"
        list_of_wanted_products = search_phrase_in_results(search.text, search.market)
        if list_of_wanted_products:
            subject = "Daily Ikea alert"    
            for element in list_of_wanted_products:
                new_message = f"{element.name} - {element.description} - {element.link}\n" 
                message_body += new_message
            send_mail(search.email.email, subject, message_body)
    return