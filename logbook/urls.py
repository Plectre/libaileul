from django.urls import path
from .import views

app_name = 'logbook'

urlpatterns = [
                path('', views.index, name='index'),
                path('form/', views.form, name="form"),
                path('delete/<int:log_id>/', views.delete, name='delete')
                ]