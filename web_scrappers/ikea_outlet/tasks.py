import os
from celery import shared_task


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from datetime import timedelta

from .models import Market, Article

from web_scrappers.celery import app
from random import randint

@shared_task
def get_all_articles():
    return Article.objects.all()

@shared_task
def scrap():
    options = Options()
    options.add_argument('---shm-size="2g"')
    driver = webdriver.Remote(command_executor='http://selenium:4444', options=options)

    markets = Market.objects.all()
    my_list = []

    for market in markets:
        link = market.webpage
        driver.get(link)
        driver.maximize_window()
        driver.implicitly_wait(2)

        while True:
            try:
                clickable = driver.find_element(By.CSS_SELECTOR,
                                                ".btn.btn--small.btn--secondary.pagination_button__wWjD6")
                ActionChains(driver) \
                    .click(clickable) \
                    .perform()
                time.sleep(1)
            except Exception:
                break

        articles = driver.find_elements(By.CLASS_NAME, "product-list_item__z6LKZ")

        for article in articles:
            try:
                name = article.get_attribute("aria-label")
                tag_link = article.find_element(By.TAG_NAME, 'a')
                link_to_product = tag_link.get_attribute('href')

                tag_class_description = article.find_element(By.CLASS_NAME, 'price-module__description')
                description = tag_class_description.text

                tag_class_price = article.find_element(By.CLASS_NAME, 'price__integer')
                price = int(tag_class_price.text)

                my_list.append((name, description, price, market, link_to_product))

            except Exception:
                print("Sth went wrong ... ")
                continue

    driver.quit()

    db_articles = Article.objects.all()
    db_articles.delete()
    for element in my_list:
        Article.objects.create(name=element[0],
                               description=element[1],
                               price=element[2],
                               market=element[3],
                               link=element[4]
                               )
    return my_list


app.conf.beat_schedule = {
    'task1':{
        'task': 'ikea_outlet.tasks.printbeat',
        'schedule': timedelta(seconds=60),
    },
    'task2':{
        'task': 'ikea_outlet.tasks.scrapbeat',
        'schedule': timedelta(seconds=120),
    },
}

@app.task(queue="queue1")
def printbeat():
    # marketname = "market1"
    # marketaddress = "address1"
    # marketwebpage = "webpage1"
    # Market.objects.create(name=marketname,
    #                       address=marketaddress,
    #                       webpage=marketwebpage)
    print("task1")
    return

@app.task(queue="queue1")
def scrapbeat():
    # options = Options()
    # options.add_argument('---shm-size="2g"')
    # driver = webdriver.Remote(command_executor='http://selenium:4444', options=options)

    # markets = Market.objects.all()
    # my_list = []

    # for market in markets:
    #     link = market.webpage
    #     driver.get(link)
    #     driver.maximize_window()
    #     driver.implicitly_wait(2)

    #     while True:
    #         try:
    #             clickable = driver.find_element(By.CSS_SELECTOR,
    #                                             ".btn.btn--small.btn--secondary.pagination_button__wWjD6")
    #             ActionChains(driver) \
    #                 .click(clickable) \
    #                 .perform()
    #             time.sleep(1)
    #         except Exception:
    #             break

    #     articles = driver.find_elements(By.CLASS_NAME, "product-list_item__z6LKZ")

    #     for article in articles:
    #         try:
    #             name = article.get_attribute("aria-label")
    #             tag_link = article.find_element(By.TAG_NAME, 'a')
    #             link_to_product = tag_link.get_attribute('href')

    #             tag_class_description = article.find_element(By.CLASS_NAME, 'price-module__description')
    #             description = tag_class_description.text

    #             tag_class_price = article.find_element(By.CLASS_NAME, 'price__integer')
    #             price = int(tag_class_price.text)

    #             my_list.append((name, description, price, market, link_to_product))

    #         except Exception:
    #             print("Sth went wrong ... ")
    #             continue

    # driver.quit()

    # db_articles = Article.objects.all()
    # db_articles.delete()
    # for element in my_list:
    #     Article.objects.create(name=element[0],
    #                            description=element[1],
    #                            price=element[2],
    #                            market=element[3],
    #                            link=element[4]
    #                            )
    print("task1")
    return