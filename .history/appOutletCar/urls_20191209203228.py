from django.urls import path, include
from django.conf.urls import url
from . import views
app_name='appOutletCar'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),

    path('listaCochesNuevos', views.listaCochesNuevos.as_view(), name='listaCochesNuevos'),
    path('listaCochesSegunda', views.listaCochesSegunda.as_view(), name='listaCochesSegunda'),
    path('listaCocheskm0', views.listaCochesKm0.as_view(), name='listaCocheskm0'),
    #path('listaCochesN', views.listaCochesN, name='listaCochesN'),
    #path('<slug:slug>/', views.detail, name='detail'),

    path('detalle_coche/<int:coche_id>/', views.DetailViewCoches, name='detail'),
    path('', views.CocheCreateView.as_view(), name='cocheCreateView'),

    path('nuestrasMarcas', views.nuestrasMarcas.as_view(), name='nuestrasMarcas'),
    path('tiposDeCoche', views.tiposDeCoche.as_view(), name='tiposDeCoche'),
    path('quienesSomos', views.quienesSomos.as_view(), name='quienesSomos'),
    
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    
        path('signup/', views.SignUp.as_view(), name='signup'),
    ]