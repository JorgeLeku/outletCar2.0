from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers
from .viewsets import CocheViewSet
app_name='appOutletCar'
router = routers.SimpleRouter()
router.register('coches', CocheViewSet)
urlpatterns = [

    path('', views.HomePageView.as_view(), name='home'),
    path('postAjax/<int:coche_id>/', views.ajax, name='ajax'),
    path('listaCochesNuevos', views.listaCochesNuevos.as_view(), name='listaCochesNuevos'),
    path('listaCochesSegunda', views.listaCochesSegunda.as_view(), name='listaCochesSegunda'),
    path('listaCocheskm0', views.listaCochesKm0.as_view(), name='listaCocheskm0'),
    #path('listaCochesN', views.listaCochesN, name='listaCochesN'),
    #path('<slug:slug>/', views.detail, name='detail'),

    path('detalle_coche/<int:coche_id>/', views.DetailViewCoches, name='detail'),
    path('', views.CocheCreateView.as_view(), name='cocheCreateView'),
    url('añadirCoche', views.añadirCoche, name='añadirCoche'),
    
    path('nuestrasMarcas', views.nuestrasMarcas.as_view(), name='nuestrasMarcas'),
    path('tiposDeCoche', views.tiposDeCoche.as_view(), name='tiposDeCoche'),
    path('quienesSomos', views.quienesSomos.as_view(), name='quienesSomos'),
    
    path('change_password/', views.change_password, name='change_password'),

    url(r'^register/$',views.register,name='register'),

    url(r'^user_login/$',views.user_login,name='user_login'),
    
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('router/', include(router.urls))
    ]
