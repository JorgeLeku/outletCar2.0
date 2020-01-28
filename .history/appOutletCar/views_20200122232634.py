from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views import View, generic
from django.template import Context, loader
from .forms import CommentForm, cocheForm, ImageForm
from .models import Coche, FotoCoche, Marca, Modelo, Lugar, TipoDeCoche, User
from .filters import FiltroCoches, FiltroCochesNuevos, FiltroCochesKm0
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from appOutletCar.forms import UserForm, UserProfileInfoForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.forms import modelformset_factory
from django.utils.translation import gettext as _

# Create your views here.
# Devuelve el listado de posts

def index(request):
    return render(request, 'añadirCoche.html')


def ajax(request, coche_id):
    post = get_object_or_404(Post, pk=post_id)
    context = { 'post': post }
    return render(request, 'ajax.html', context)
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


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
    usuarios = request.user
    ImageFormSet = modelformset_factory(FotoCoche, form=ImageForm, extra=5)
    form=None
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = cocheForm(data=request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=FotoCoche.objects.none())
        # check whether it's valid:
        if form.is_valid() and formset.is_valid():
           
            coche = form.save(commit=False)
            coche.usuario= usuarios
            coche.save()
            for form in formset.cleaned_data:
                image = form['image']
                photo = FotoCoche(coche=coche, fotoCoche=image)
                photo.save()

            return HttpResponseRedirect(reverse_lazy('appOutletCar:home'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = cocheForm()
        formset = ImageFormSet(queryset=FotoCoche.objects.none())
    return render(request, 'añadirCoche.html', {'form': form, 'formset': formset})

def DetailViewCoches(request, coche_id):
    template_name = 'coche_detalle.html'
    coches = get_object_or_404(Coche, id=coche_id)
    usuario = request.user
    comments = coches.comments.filter(active=True)
    fotoCoche = FotoCoche.objects.filter(coche=coches)
    new_comment = None
    # Comment posted
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current coche to the comment
            new_comment.coche = coches
            new_comment.usuario = usuario
            # Save the comment to the database
            
            new_comment.save()
    else:
        comment_form = CommentForm()

    

    return render(request, template_name, {'coche': coches,
                                            'fotoCoches': fotoCoche,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

    





def index(request):
    return render(request,'appOutletCar/home.html')



@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
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
                return HttpResponseRedirect(reverse('home'))
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

@login_required
class quienesSomos(TemplateView):

    template_name = "quienesSomos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    




from .serializer import CocheSerializer

from rest_framework import generics



class CocheList(generics.ListCreateAPIView):
  
    queryset = Coche.objects.all()
    serializer_class = CocheSerializer
class CocheDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coche.objects.all()
    serializer_class = CocheSerializer
