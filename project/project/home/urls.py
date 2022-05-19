from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
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
    path("login",views.login,name='login'),
    path("dashboard",views.dashboard,name='dashboard'),
    path("selling",views.selling,name='selling'),
    path("book-officer",views.book_officer,name='book_officer'),
    path("officers/101",views.officers101,name='officers101'),
    path("officers/102",views.officers102,name='officers102'),
    path("officers/103",views.officers103,name='officers103'),
    path("officers/104",views.officers104,name='officers104'),
    path("officers/105",views.officers105,name='officers105'),
    path("survey",views.survey,name='survey'),
    path("profile",views.profile,name='profile'),
    path("grow-crop",views.grow_crop,name='grow_crop'),
    path("videos",views.videos,name='videos'),
]