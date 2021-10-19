#  hello/urls.py

from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('poema_1', views.poema_1_view, name='poema_1'),
    path('poema_2', views.poema_2_view, name='poema_2'),
    path('poema_3', views.poema_3_view, name='poema_3')
]