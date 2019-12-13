from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views import View, generic
from django.template import Context, loader
from .forms import CommentForm, cocheForm
from .models import Coche, FotoCoche, Marca, Modelo, Lugar, TipoDeCoche, User
from .filters import FiltroCoches, FiltroCochesNuevos, FiltroCochesKm0
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from appOutletCar.forms import UserForm, UserProfileInfoForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
# Devuelve el listado de posts
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Coche.objects.all()[:5]
        return context



class listaCochesSegunda(ListView):
    model = Coche
    template_name = 'cochesSegundaMano.html'

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



def añadirCoche(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = cocheForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = cocheForm()

    return render(request, 'añadirCoche.html', {'form': form})

def DetailViewCoches(request, coche_id):
    template_name = 'coche_detalle.html'
    coche = get_object_or_404(Coche, id=coche_id)
    usuario = request.user
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
            new_comment.usuario = usuario
            # Save the comment to the database
            
            new_comment.save()
    else:
        comment_form = CommentForm()

    

    return render(request, template_name, {'coche': coche,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

    





def index(request):
    return render(request,'appOutletCar/index.html')



@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'appOutletCar/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'appOutletCar/login.html', {})


class nuestrasMarcas(ListView):

    template_name = "nuestrasMarcas.html"
    model = Marca
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class tiposDeCoche(ListView):

    template_name = "tiposDeCoche.html"
    model = TipoDeCoche
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class quienesSomos(TemplateView):

    template_name = "quienesSomos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
