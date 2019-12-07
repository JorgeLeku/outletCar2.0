from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views import View
from django.template import Context, loader
from .forms import CommentForm
from .models import Coche, FotoCoche, Marca, Modelo, Lugar
from .filters import FiltroCoches, FiltroCochesNuevos, FiltroCochesKm0
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

class listaCochesSegunda(ListView):
    model = Coche
    template_name = 'cochesNuevos.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['filter']=FiltroCoches(self.request.GET, queryset=self.get_queryset())
        return context
class listaCochesNuevos(ListView):
    model=Coche
    template_name = 'cochesNuevos.html'
    #model=get_list_or_404(coche.objects.filter(estado="Segunda mano"))
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['filter']=FiltroCochesNuevos(self.request.GET, queryset=self.get_queryset())
        return context

class listaCochesKm0(ListView):
    template_name = 'cocheskm0.html'
    model=Coche

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['filter']=FiltroCochesKm0(self.request.GET, queryset=self.get_queryset())
        return context

class nuestrasMarcas(TemplateView):

    template_name = "nuestrasMarcas.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class tiposDeCoche(TemplateView):

    template_name = "tiposDeCoche.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class quienesSomos(TemplateView):

    template_name = "quienesSomos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CocheCreateView(CreateView):
    model = Coche
    fields = ('n_bastidor', 'color', 'n_km')

#class listaCochesKm0(ListView):
#    model = Coche
#    template_name = "cocheskm0.html"
#    paginate_by = 10

#    def get_queryset(self):
#        filter_val = self.request.GET.get('filter', 'n_bastidor')
#        order = self.request.GET.get('orderby', 'n_bastidor')
#        new_context = Coche.objects.filter(
#            color=filter_val,
#        ).order_by(order)
#        return new_context

#    def get_context_data(self, **kwargs):
#        context = super(listaCochesKm0, self).get_context_data(**kwargs)
#        context['filter'] = self.request.GET.get('filter', 'n_bastidor')
#        context['orderby'] = self.request.GET.get('orderby', 'n_bastidor')
#        return context


def DetailViewCoches(request, slug):
    template_name = 'coche_detalle.html'
    coche = get_object_or_404(Coche, slug=slug)
    comments = coche.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current coche to the comment
            new_comment.coche = coche
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'coche': coche,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def detail(request, post_id):
    coche = get_object_or_404(Coche, pk=n_bastidor)
    context = { 'coche': coche }
    return render(request, 'coche_detalle.html', context)

class login(TemplateView):

    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class register(TemplateView):

    template_name = "registro.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class reset_password(TemplateView):
    template_name = "reset_password.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class password_reset_complete(TemplateView):
    template_name = "password_reset_complete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class password_reset_confirm(TemplateView):
    template_name = "password_reset_confirm.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class password_reset_done(TemplateView):
    template_name = "password_reset_done.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class password_reset_email(TemplateView):
    template_name = "password_reset_email.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class password_reset_form(TemplateView):
    template_name = "password_reset_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

