from django.shortcuts import render
from .models import Coche
from django.shortcuts import get_object_or_404, get_list_or_404
# Create your views here.
# Devuelve el listado de posts
def index(request):
    posts = get_list_or_404(Coche.objects.order_by('anyo'))
    context = { 'lista_posts': posts}
    return render(request, 'index.html', context)