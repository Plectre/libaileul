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

def weather(request):
    print("appel display weather")
    weather = get_weather()
    if weather:
        return render(request, 'hangar/weather.html', {"weather": weather})
    else:
        return render(request, 'hangar/weather.html')


def map(request):
    return(request, 'hangar/map.html')
