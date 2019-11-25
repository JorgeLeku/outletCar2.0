from django.shortcuts import render
from .models import Coche, FotoCoche, Marca, Modelo, Lugar
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .filters import FiltroCoches
from django.views.generic import CreateView
# Create your views here.
# Devuelve el listado de posts
class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Coche.objects.all()[:5]
        return context

def listaCochesN(request):
    coche = get_list_or_404(Coche.objects.order_by('n_bastidor').filter(estado="Segunda mano"))
    context = { 'lista_cochesN': coche }
    return render(request, 'cochesNuevos.html', context)

class listaCochesNpr(ListView):
    model = Coche
    template_name = 'cochesNuevos.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['filter']=FiltroCoches(self.request.GET, queryset=self.get_queryset())
        return context

class CocheCreateView(CreateView):
    model = Coche
    fields = ('n_bastidor', 'color', 'n_km')