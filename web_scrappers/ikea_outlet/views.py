from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from .models import Category, Market, Article
from .forms import MarketAddForm
from .forms import AprovingForm, APROVING_CHOICES

from .forms import CategoryAddForm

from .forms import ScrapForm

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


class About(View):
    def get(self, request):
        ctx = {}
        return render(request, 'about.html', ctx)

    def post(self, request):
        pass


class InvalidData(View):
    def get(self, request):
        ctx = {}
        return render(request, 'invalid_data.html', ctx)

    def post(self, request):
        pass


class MarketsList(View):
    def get(self, request):
        markets = Market.objects.all()
        ctx = {'markets':markets}
        return render(request, 'markets_list.html', ctx)

    def post(self, request):
        pass


class MarketAdd(View):
    def get(self, request):
        form = MarketAddForm()
        ctx = {'form': form}
        return render(request, 'market_add.html', ctx)

    def post(self, request):
        form = MarketAddForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            webpage= form.cleaned_data['webpage']
            Market.objects.create(name=name,
                                  address=address,
                                  webpage=webpage)
            return redirect('markets_list')
        else:
            HttpResponseRedirect('invalid_data')


class MarketDelete(View):
    def get(self, request, market_id):
        form = AprovingForm()
        ctx = {'form': form}
        return render(request, 'market_delete.html', ctx)

    def post(self, request, market_id):
        form = AprovingForm(request.POST)
        if form.is_valid():
            choice_dict = dict(APROVING_CHOICES)
            choice = choice_dict[int(form.cleaned_data['choice'])]
            if choice == 'yes':
                market = Market.objects.get(id=market_id)
                market.delete()
            return redirect('markets_list')
        else:
            HttpResponseRedirect('invalid_data')


class MarketEdit(View):
    def get(self, request, market_id):
        market = Market.objects.get(id=market_id)
        form = MarketAddForm()
        ctx = {'form': form, 'market': market}
        return render(request, 'market_edit.html', ctx)

    def post(self, request, market_id):
        form = MarketAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            webpage = form.cleaned_data['webpage']
            market = Market.objects.get(id=market_id)
            market.name = name
            market.address = address
            market.webpage = webpage
            market.save()
            return redirect('markets_list')
        else:
            HttpResponseRedirect('invalid_data')


class CategoriesList(View):
    def get(self, request):
        categories = Category.objects.all()
        ctx = {'categories': categories}
        return render(request, 'categories_list.html', ctx)

    def post(self, request):
        pass


class CategoryAdd(View):
    def get(self, request):
        form = CategoryAddForm()
        ctx = {'form': form}
        return render(request, 'category_add.html', ctx)

    def post(self, request):
        form = CategoryAddForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            symbol = form.cleaned_data['symbol']
            Category.objects.create(name=name,
                                    symbol=symbol)
            return redirect('categories_list')
        else:
            HttpResponseRedirect('invalid_data')


class CategoryDelete(View):
    def get(self, request, category_id):
        form = AprovingForm()
        ctx = {'form': form}
        return render(request, 'category_delete.html', ctx)

    def post(self, request, category_id):
        form = AprovingForm(request.POST)
        if form.is_valid():
            choice_dict = dict(APROVING_CHOICES)
            choice = choice_dict[int(form.cleaned_data['choice'])]
            if choice == 'yes':
                category = Category.objects.get(id=category_id)
                category.delete()
            return redirect('categories_list')
        else:
            HttpResponseRedirect('invalid_data')


class CategoryEdit(View):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        form = CategoryAddForm()
        ctx = {'form': form, 'category': category}
        return render(request, 'category_edit.html', ctx)

    def post(self, request, category_id):
        form = CategoryAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            symbol = form.cleaned_data['symbol']
            category = Category.objects.get(id=category_id)
            category.name = name
            category.symbol = symbol
            category.save()
            return redirect('categories_list')
        else:
            HttpResponseRedirect('invalid_data')


class StartScrap(View):
    def get(self, request):
        form = AprovingForm()
        ctx = {'form': form}
        return render(request, 'start_scrap.html', ctx)

    def post(self, request):
        options = Options()
        options.binary_location = "/home/marcin/workspace/portfolio/chromedriver/chromedriver.exe"
        driver = webdriver.Chrome(options=options)

        categories = Category.objects.all()
        markets = Market.objects.all()
        my_list = []

        for market in markets:
            for category in categories:
                # my_list.append(market.webpage + '&category=' + category.symbol)

                link = market.webpage + '&category=' + category.symbol
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


                 # clickable = driver.find_element(By.CSS_SELECTOR, ".btn.btn--small.btn--secondary.pagination_button__wWjD6")
                # while clickable is not None:
                #     ActionChains(driver) \
                #         .click(clickable) \
                #         .perform()
                #     time.sleep(2)
                #     try:
                #         clickable = driver.find_element(By.CSS_SELECTOR,
                #                                         ".btn.btn--small.btn--secondary.pagination_button__wWjD6")
                #     except Exception:
                #         break

                articles = driver.find_elements(By.CLASS_NAME, "product-list_item__z6LKZ")

                for article in articles:
                    try:
                        name = article.get_attribute("aria-label")

                        tag_link = article.find_element(By.TAG_NAME, 'a')
                        link = 'https://www.ikea.com/pl/pl/customer-service/services/okazje-na-okraglo-pub63b48c50' + tag_link.get_attribute('href')

                        tag_class_description = article.find_element(By.CLASS_NAME, 'price-module__description')
                        description = tag_class_description.text

                        tag_class_price = article.find_element(By.CLASS_NAME, 'price__integer')
                        price = tag_class_price.text

                        # tag_class_status = article.find_element(By.CLASS_NAME, 'status__label')
                        # location = tag_class_status.text

                        my_list.append((name, description, price, market, link, category))

                    except Exception:
                        print("sth went wrong")
                        continue

        driver.quit()

        db_articles = Article.objects.all()
        db_articles.delete()
        for element in my_list:
            Article.objects.create(name=element[0],
                                   description=element[1],
                                   price=element[2],
                                   market=element[3],
                                   link=element[4],
                                   categories=element[5])

        ctx = {"my_list": my_list, "amount_of_products": len(my_list)}
        return render(request, 'finish_scrap.html', ctx)


class ArticlesAll(View):
    def get(self, request):
        articles = Article.objects.all()
        ctx = {'articles': articles, 'amount_of_products': len(articles)}
        return render(request, "articles_all.html", ctx)

    def post(self, request):
        pass
