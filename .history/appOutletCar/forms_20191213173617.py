from .models import Comment, FotoCoche
from django import forms
from appOutletCar.models import UserProfileInfo
from django.contrib.auth.models import User
from .models import Coche

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = FotoCoche
        fields = ('image', )
        
class cocheForm(forms.ModelForm):

    class Meta:
        model = Coche
        fields = ('modelo', 'anyo','estado', 'n_bastidor','color', 'n_km','combustible', 'potencia','precio', 'cambio','consumo', 'comentario','lugar')

