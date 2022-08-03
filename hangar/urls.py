
from django.urls import path
from . import views

app_name="hangar"

urlpatterns = [
    path('', views.index, name='index'),
    path('ecole/', views.ecole, name='ecole'),
    path('baptemes/', views.baptemes, name='baptemes'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('weather/', views.weather, name='weather')
]