from django.urls import path, include
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
    path('login', views.login.as_view(), name='login'),
    path('register', views.register.as_view(), name='register'),
    path('reset_password', views.reset_password.as_view(), name='reset_password'),
    path('password_reset_complete', views.password_reset_complete.as_view(), name='password_reset_complete'),
    path('password_reset_confirm', views.password_reset_confirm.as_view(), name='password_reset_confirm'),
    path('password_reset_done', views.password_reset_done.as_view(), name='password_reset_done'),
    path('password_reset_email', views.password_reset_email.as_view(), name='password_reset_email'),
    path('password_reset_form', views.password_reset_form.as_view(), name='password_reset_form'),

    ]