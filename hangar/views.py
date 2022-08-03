from multiprocessing import context
from django.shortcuts import render
from .models import Articles
from .services import get_weather

def index(request):
    articles = Articles
    weather = get_weather()
    article = articles.objects.all()
    context = {
        'articles': article,
        'weathers': weather,
    }
    return render(request, "hangar/index.html", context)

def detail(request, id):
    articles = Articles
    details = articles.objects.get(pk=id)
    print(f"{details}")
    context = {
        'details': details,
    }
    return render(request, 'hangar/detail.html', context)

def ecole(request):
    return render(request, 'hangar/ecole.html')

def baptemes(request):
    articles = Articles
    article = articles.objects.get(title="Les baptêmes de l’air")
    context = {
        'article': article,
    }
    return render(request, 'hangar/baptemes.html', context)

def weather(request):
    print("appel display weather")
    weather = get_weather()

    print(weather)
    return render(request, 'hangar/weather.html', {"weather": weather})
