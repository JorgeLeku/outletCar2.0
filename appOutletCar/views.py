from django.shortcuts import render
from .models import Coche
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic.base import TemplateView
# Create your views here.
# Devuelve el listado de posts
def index(request):
    posts = get_list_or_404(Coche.objects.order_by('anyo'))
    context = { 'lista_posts': posts}
    return render(request, 'index.html', context)

class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Coche.objects.all()[:5]
        return context