from django.shortcuts import render
from django.views import View

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class Main(View):
    def get(self, request):
        ctx = {}
        return render(request, 'main.html', ctx)

    def post(self, request):
        pass


class ResultTable1(View):
    def get(self, request):

        options = Options()
        options.binary_location = "/home/marcin/workspace/portfolio/chromedriver/chromedriver.exe"

        driver = webdriver.Chrome(options=options)
        driver.get('https://www.ikea.com/pl/pl/customer-service/services/okazje-na-okraglo-pub63b48c50#/?store=307')
        driver.maximize_window()
        driver.implicitly_wait(5)

        clickable = driver.find_element(By.CSS_SELECTOR, ".btn.btn--small.btn--secondary.pagination_button__wWjD6")
        while clickable is not None:
            ActionChains(driver) \
                .click(clickable) \
                .perform()
            time.sleep(2)
            try:
                clickable = driver.find_element(By.CSS_SELECTOR,
                                                ".btn.btn--small.btn--secondary.pagination_button__wWjD6")
            except Exception:
                break

        my_list = []
        articles = driver.find_elements(By.CLASS_NAME, "product-list_item__z6LKZ")
        for article in articles:
            name = article.get_attribute("aria-label")

            tag_link = article.find_element(By.TAG_NAME, 'a')
            link = 'https://www.ikea.com/pl/pl/customer-service/services/okazje-na-okraglo-pub63b48c50' + tag_link.get_attribute('href')

            tag_class_description = article.find_element(By.CLASS_NAME, 'price-module__description')
            description = tag_class_description.text

            tag_class_price = article.find_element(By.CLASS_NAME, 'price__integer')
            price = tag_class_price.text

            tag_class_status = article.find_element(By.CLASS_NAME, 'status__label')
            status = tag_class_status.text

            my_list.append((name, description, price, status, link))


        driver.quit()

        ctx = {"my_list": my_list, "amount_of_products": len(my_list)}
        return render(request, 'result_table_1.html', ctx)

    def post(self, request):
        pass
