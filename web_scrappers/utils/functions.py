from ikea_outlet.models import Market, Article

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def scrap():
    options = Options()
    options.add_argument('---shm-size="2g"')
    driver = webdriver.Remote(command_executor='http://selenium:4444', options=options)

    markets = Market.objects.all()
    result_list = []

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

                result_list.append((name, description, price, market, link_to_product))

            except Exception:
                print("Sth went wrong ... ")
                continue
    driver.quit()
    return result_list


def clear_db():
    db_articles = Article.objects.all()
    db_articles.delete()
    return


def save_result_to_db(scrapped_list):
    for element in scrapped_list:
        Article.objects.create(name=element[0],
                               description=element[1],
                               price=element[2],
                               market=element[3],
                               link=element[4]
                               )
    return



def search_phrase_in_results(phrase, market):
    list_of_wanted_products = []
    articles = Article.objects.filter(market=market) #Dodać filtr marketu (!!!!!!!!!!!!!!!!)
    for article in articles:
        if phrase.upper() in article.name.upper() or phrase.upper() in article.description.upper():
            list_of_wanted_products.append(article)
    return list_of_wanted_products



def send_mail(recipient_email, subject, message_body):
    host = 'smtp.yandex.com'
    port = 465
    login = 'ikeabotalert'
    app_password = 'trudpsfzlcyghoes' # password generated in Yandex
    from_addr = 'ikeabotalert@yandex.com'

    # Create a multipart message
    message = MIMEMultipart()
    message['From'] = from_addr
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(message_body, 'plain'))



    smtpObj=smtplib.SMTP_SSL(host, port)
    code, msg = smtpObj.ehlo()
    if code == 250:
        code_auth, msg_auth = smtpObj.login(login, app_password)
        if code_auth == 235:
            smtpObj.sendmail(from_addr, recipient_email, message.as_string())
            smtpObj.quit()
        else:
            print(code_auth, msg_auth)
    else:
        print(code, msg)
    return