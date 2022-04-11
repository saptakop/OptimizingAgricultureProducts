from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("news", views.news, name='news'),
    path("project", views.project, name='project'),
    path("project/tool", views.tool, name='tool'),
    path("faq", views.faq, name='faq'),
    path("project/tool/rice", views.rice, name='rice'),
    path("project/tool/mothbeans", views.mothbeans, name='mothbeans'),
    path("news-farmer", views.news_farmer, name='news-farmer'),
    path("news-schemes", views.news_schemes, name='news-schemes'),
    path("news-crops", views.news_crops, name='news-crops'),
    path("news-price", views.news_price, name='news-price'),
    path("news-business", views.news_business, name='news-business'),
    path("news-politics", views.news_politics, name='news-politics'),
]