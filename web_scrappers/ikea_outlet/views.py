from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from .models import Market, Article, Person, Search
from .forms import MarketAddForm, UserAddForm, SearchAddForm
from .forms import AprovingForm, APROVING_CHOICES
from .forms import ArticlesFilterForm

from utils.functions import scrap



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
        ctx = {'markets': markets}
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


class UsersList(View):
    def get(self, request):
        users = Person.objects.all()
        ctx = {'users': users}
        return render(request, 'users_list.html', ctx)

    def post(self, request):
        pass


class UserAdd(View):
    def get(self, request):
        form = UserAddForm()
        ctx = {'form': form}
        return render(request, 'user_add.html', ctx)

    def post(self, request):
        form = UserAddForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            
            Person.objects.create(username=username,
                                  email=email)
            return redirect('users_list')
        else:
            HttpResponseRedirect('invalid_data')


class UserDelete(View):
    def get(self, request, user_id):
        form = AprovingForm()
        ctx = {'form': form}
        return render(request, 'user_delete.html', ctx)

    def post(self, request, user_id):
        form = AprovingForm(request.POST)
        if form.is_valid():
            choice_dict = dict(APROVING_CHOICES)
            choice = choice_dict[int(form.cleaned_data['choice'])]
            if choice == 'yes':
                user = Person.objects.get(id=user_id)
                user.delete()
            return redirect('users_list')
        else:
            HttpResponseRedirect('invalid_data')


class UserEdit(View):
    def get(self, request, user_id):
        user = Person.objects.get(id=user_id)
        form = UserAddForm()
        ctx = {'form': form, 'user': user}
        return render(request, 'user_edit.html', ctx)

    def post(self, request, user_id):
        form = UserAddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = Person.objects.get(id=user_id)
            user.name = username
            user.email = email
            user.save()
            return redirect('users_list')
        else:
            HttpResponseRedirect('invalid_data')


class SearchList(View):
    def get(self, request):
        searches = Search.objects.all()
        ctx = {'searches': searches}
        return render(request, 'search_list.html', ctx)

    def post(self, request):
        pass


class SearchAdd(View):
    def get(self, request):
        form = SearchAddForm()
        ctx = {'form': form}
        return render(request, 'search_add.html', ctx)

    def post(self, request):
        form = SearchAddForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            market = form.cleaned_data['market']
            text = form.cleaned_data['text']
            Search.objects.create(email=email,
                                  market=market,
                                  text=text)
            return redirect('search_list')
        else:
            HttpResponseRedirect('invalid_data')


class SearchDelete(View):
    def get(self, request, search_id):
        form = AprovingForm()
        ctx = {'form': form}
        return render(request, 'search_delete.html', ctx)

    def post(self, request, search_id):
        form = AprovingForm(request.POST)
        if form.is_valid():
            choice_dict = dict(APROVING_CHOICES)
            choice = choice_dict[int(form.cleaned_data['choice'])]
            if choice == 'yes':
                user = Search.objects.get(id=search_id)
                user.delete()
            return redirect('search_list')
        else:
            HttpResponseRedirect('invalid_data')


class SearchEdit(View):
    def get(self, request, search_id):
        search = Search.objects.get(id=search_id)
        form = SearchAddForm()
        ctx = {'form': form, 'search': search}
        return render(request, 'search_edit.html', ctx)

    def post(self, request, search_id):
        form = SearchAddForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            market = form.cleaned_data['market']
            text = form.cleaned_data['text']
            search = Search.objects.get(id=search_id)
            search.email = email
            search.market = market
            search.text = text
            search.save()
            return redirect('search_list')
        else:
            HttpResponseRedirect('invalid_data')


class StartScrap(View):
    def get(self, request):
        form = AprovingForm()
        ctx = {'form': form}
        return render(request, 'start_scrap.html', ctx)

    def post(self, request):
        my_list = scrap()
        ctx = {"my_list": my_list, "amount_of_products": len(my_list)}
        return render(request, 'finish_scrap.html', ctx)


class ArticlesAll(View):
    def get(self, request):
        articles = Article.objects.all()
        ctx = {'articles': articles, 'amount_of_products': len(articles)}
        return render(request, "results_articles_all.html", ctx)

    def post(self, request):
        pass


class ArticlesFilter(View):
    def get(self, request):
        form = ArticlesFilterForm()
        ctx = {'form': form}
        return render(request, "results_articles_filter_form.html", ctx)

    def post(self, request):
        form = ArticlesFilterForm(request.POST)
        if form.is_valid():
            markets_id = form['markets'].data
            print(len(markets_id))

            if len(markets_id) == 0:
                markets = Market.objects.all()
            else:
                markets = Market.objects.filter(pk__in=markets_id)

            articles = Article.objects.filter(market__in=markets)

            ctx = {'articles': articles, 'amount_of_products': len(articles)}
            return render(request, "results_articles_filter.html", ctx)
        else:
            return render(request, "invalid_data.html")



