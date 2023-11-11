from django.conf import settings
from .celery import app

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

from .models import Market, Article

from celery.schedules import crontab



@app.task
def scrap():
   
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # options = Options()
    # options.add_argument('--no-sandbox')
    # options.add_argument('--window-size=1920,1080')
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

    # service = webdriver.ChromeService(executable_path='/usr/local/bin/chromedriver-linux64/chromedriver')


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
                # store = link.split("?")[1]
                tag_link = article.find_element(By.TAG_NAME, 'a')
                link_to_product = tag_link.get_attribute('href')
                # link = 'https://www.ikea.com/pl/pl/customer-service/services/okazje-na-okraglo-pub63b48c50' + tag_link.get_attribute('href') + "?" +

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


