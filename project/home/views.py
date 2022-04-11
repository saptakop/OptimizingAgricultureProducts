import imp
from django.shortcuts import render, HttpResponse
import pandas as pd
from home.models import Contact
from datetime import datetime
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        'name1':None,
        'email1':None,
        'desc1':None,
        'date1':None,
        'name2':None,
        'email2':None,
        'desc2':None,
        'date2':None,
        'name3':None,
        'email3':None,
        'desc3':None,
        'date3':None,
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,desc=desc,date=datetime.now())
        contact.save()

        messages.success(request, 'Your Message Has Been Sent.')
    
    for obj in Contact.objects.all():
        context['name3'] = context['name2']
        context['email3'] = context['email2']
        context['desc3'] = context['desc2']
        context['date3'] = context['date2']

        context['name2'] = context['name1']
        context['email2'] = context['email1']
        context['desc2'] = context['desc1']
        context['date2'] = context['date1']

        context['name1'] = obj.name
        context['email1'] = obj.email
        context['desc1'] = obj.desc
        context['date1'] = obj.date

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    #return render(request, 'services.html')
    return HttpResponse('503 Service Not Available')

def news(request):
    return render(request, 'news.html')

def news_farmer(request):
    return render(request, 'news-farmer.html')

def news_schemes(request):
    return render(request, 'news-schemes.html')

def news_crops(request):
    return render(request, 'news-crops.html')

def news_price(request):
    return render(request, 'news-price.html')

def news_business(request):
    return render(request, 'news-business.html')

def news_politics(request):
    return render(request, 'news-politics.html')

def project(request):
    return render(request, 'project.html')
    
def tool(request):
    result=None
    nitrogen=0.0
    phosphorous=0.0
    potassium=0.0
    temp=0.0
    humidity=0.0
    pH=0.0
    rainfall=0.0
    modelName = 'Linear Regression'
    if request.method == 'POST':
        nitrogen = float(request.POST.get('nitrogen'))
        phosphorous = float(request.POST.get('phosphorous'))
        potassium = float(request.POST.get('potassium'))
        temp = float(request.POST.get('temp'))
        humidity = float(request.POST.get('humidity'))
        pH = float(request.POST.get('pH'))
        rainfall = float(request.POST.get('rainfall'))
        modelName = str(request.POST.get('model'))

        if modelName == 'Logistic Regression':
            model = pd.read_pickle('./new_model.pickle')
        if modelName == 'Linear Regression':
            model = pd.read_pickle('./new_model_dt.pickle')
        elif modelName == 'Decision Tree':
            model = pd.read_pickle('./new_model_dt.pickle')
        else:
            model = pd.read_pickle('./new_model_dt.pickle')

        result = model.predict([[nitrogen,phosphorous,potassium,temp,humidity,pH,rainfall]])
        result = result[0]
    context={
        'nitrogen':nitrogen,
        'phosphorous':phosphorous,
        'potassium':potassium,
        'temp':temp,
        'humidity':humidity,
        'pH':pH,
        'rainfall':rainfall,
        'result':result,
        'model':modelName
    }
    return render(request, 'tool.html', context)

def predict(request):
    result=1
    if request.method == 'POST':
        nitrogen = float(request.POST.get('nitrogen'))
        phosphorous = float(request.POST.get('phosphorous'))
        potassium = float(request.POST.get('potassium'))
        temp = float(request.POST.get('temp'))
        humidity = float(request.POST.get('humidity'))
        pH = float(request.POST.get('pH'))
        rainfall = float(request.POST.get('rainfall'))
        modelName = str(request.POST.get('model'))

        if modelName == 'Linear Regression':
            model = pd.read_pickle('/Users/rajdippal/Desktop/django/project/new_model.pickle')
        elif modelName == 'Decision Tree':
            model = pd.read_pickle('/Users/rajdippal/Desktop/django/project/new_model_dt.pickle')
        else:
            model = pd.read_pickle('/Users/rajdippal/Desktop/django/project/new_model_knn.pickle')

        result = model.predict([[nitrogen,phosphorous,potassium,temp,humidity,pH,rainfall]])
    context={
        'nitrogen':nitrogen,
        'phosphorous':phosphorous,
        'potassium':potassium,
        'temp':temp,
        'humidity':humidity,
        'pH':pH,
        'rainfall':rainfall,
        'result':result,
        'model':modelName
    }
    return render(request, 'predict.html',context)

def faq(request):
    return render(request, 'faq.html')


def rice(request):
    return render(request, 'rice.html')

def mothbeans(request):
    return render(request, 'mothbeans.html')