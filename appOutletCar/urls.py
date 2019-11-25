from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('listaCochesN', views.listaCochesNpr.as_view(), name='listaCochesN'),
    #path('listaCochesN', views.listaCochesN, name='listaCochesN'),
    path('', views.CocheCreateView.as_view(), name='cocheCreateView')
    ]