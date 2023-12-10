from django.contrib import admin
from django.urls import path

from ikea_outlet.views import Main, About
from ikea_outlet.views import InvalidData
from ikea_outlet.views import MarketsList, MarketAdd, MarketEdit, MarketDelete
from ikea_outlet.views import StartScrap
from ikea_outlet.views import ArticlesAll, ArticlesFilter
from ikea_outlet.views import UsersList, UserAdd, UserEdit, UserDelete
from ikea_outlet.views import SearchList, SearchAdd, SearchEdit, SearchDelete



urlpatterns = [
    path('admin/', admin.site.urls),
    path('web_scrappers/main/', Main.as_view(), name='main'),
    path('web_scrappers/about/', About.as_view(), name='about'),

    path('web_scrappers/invaliddata/', InvalidData.as_view(), name='invalid_data'),

    path('web_scrappers/markets_list/', MarketsList.as_view(), name='markets_list'),
    path('web_scrappers/market_add/', MarketAdd.as_view(), name='market_add'),
    path('web_scrappers/market_edit/<int:market_id>', MarketEdit.as_view(), name='market_edit'),
    path('web_scrappers/market_delete/<int:market_id>', MarketDelete.as_view(), name='market_delete'),

    path('web_scrappers/start_scrap/', StartScrap.as_view(), name='start_scrap'),

    path('web_scrappers/results_articles_all/', ArticlesAll.as_view(), name='results_articles_all'),
    path('web_scrappers/results_articles_filter/', ArticlesFilter.as_view(), name='results_articles_filter'),

    path('web_scrappers/users_list/', UsersList.as_view(), name='users_list'),
    path('web_scrappers/user_add/', UserAdd.as_view(), name='user_add'),
    path('web_scrappers/user_edit/<int:user_id>', UserEdit.as_view(), name='user_edit'),
    path('web_scrappers/user_delete/<int:user_id>', UserDelete.as_view(), name='user_delete'),

    path('web_scrappers/search_list/', SearchList.as_view(), name='search_list'),
    path('web_scrappers/search_add/', SearchAdd.as_view(), name='search_add'),
    path('web_scrappers/search_edit/<int:search_id>', SearchEdit.as_view(), name='search_edit'),
    path('web_scrappers/search_delete/<int:search_id>', SearchDelete.as_view(), name='search_delete'),
]

