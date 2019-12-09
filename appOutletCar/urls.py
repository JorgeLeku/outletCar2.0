from django.urls import path, include
from django.conf.urls import url
from . import views
app_name='appOutletCar'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('listaCochesNuevos', views.listaCochesNuevos.as_view(), name='listaCochesNuevos'),
    path('listaCochesSegunda', views.listaCochesSegunda.as_view(), name='listaCochesSegunda'),
    #path('listaCochesN', views.listaCochesN, name='listaCochesN'),
    path('', views.CocheCreateView.as_view(), name='cocheCreateView'),
    path('listaCocheskm0', views.listaCochesKm0.as_view(), name='listaCocheskm0'),
    path('nuestrasMarcas', views.nuestrasMarcas.as_view(), name='nuestrasMarcas'),
    path('tiposDeCoche', views.tiposDeCoche.as_view(), name='tiposDeCoche'),
    path('quienesSomos', views.quienesSomos.as_view(), name='quienesSomos'),
    #path('<slug:slug>/', views.detail, name='detail'),
    path('coche_detalle/<str:n_bastidor>/', views.detail, name='detail'),
     url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    ]