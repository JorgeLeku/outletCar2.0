from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('listaCochesNuevos', views.listaCochesNuevos.as_view(), name='listaCochesNuevos'),
    path('listaCochesSegunda', views.listaCochesSegunda.as_view(), name='listaCochesSegunda'),
    #path('listaCochesN', views.listaCochesN, name='listaCochesN'),
    path('', views.CocheCreateView.as_view(), name='cocheCreateView'),
    path('listaCocheskm0', views.listaCochesKm0.as_view(), name='listaCocheskm0'),
    ]