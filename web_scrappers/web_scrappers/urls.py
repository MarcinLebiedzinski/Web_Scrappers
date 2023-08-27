"""web_scrappers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ikea_outlet.views import Main, About
from ikea_outlet.views import MarketsList, MarketAdd, MarketEdit, MarketDelete
from ikea_outlet.views import ResultTable1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('web_scrappers/main/', Main.as_view(), name='main'),
    path('web_scrappers/about/', About.as_view(), name='about'),


    path('web_scrappers/markets_list/', MarketsList.as_view(), name='markets_list'),
    path('web_scrappers/market_add/', MarketAdd.as_view(), name='market_add'),
    path('web_scrappers/market_edit/<int:market_id>', MarketEdit.as_view(), name='market_edit'),
    path('web_scrappers/market_delete/<int:market_id>', MarketDelete.as_view(), name='market_delete'),

    path('web_scrappers/ikea_results/', ResultTable1.as_view(), name='result_table_1'),

]
