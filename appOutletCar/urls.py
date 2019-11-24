from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('listaCochesN', views.listaCochesN, name='listaCochesN'),
    ]