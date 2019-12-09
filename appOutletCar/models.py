from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User


# Create your models here.
class Lugar(models.Model):
    cod_ciudad = models.CharField(null=False, primary_key=True, max_length=4)
    ciudad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)

    def __str__(self):

        return self.cod_ciudad


class Marca(models.Model):
    nombre_Marca = models.CharField(max_length=100, null=False, primary_key=True)
    descripcion = models.CharField(max_length=5000)
    fecha_creacion = models.DateField()

    def __str__(self):

        return self.nombre_Marca


class Modelo(models.Model):
    nombre_Modelo = models.CharField(max_length=100, null=False, primary_key=True)
    categoria = models.CharField(max_length=100)
    traccion = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):

        return self.nombre_Modelo

class Usuario(models.Model):
    correo = models.CharField(max_length=100, null=False, primary_key=True)
    nombre_usuario = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.IntegerField()
    contrasenya = models.CharField(max_length=100)

    def __str__(self):

        return self.correo


class Coche(models.Model):
    n_bastidor = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    anyo = models.IntegerField()
    n_km = models.IntegerField()
    combustible = models.CharField(max_length=100)
    potencia = models.IntegerField()
    precio = models.FloatField()
    cambio = models.CharField(max_length=100)
    consumo = models.FloatField()
    comentario = models.CharField(max_length=1000)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado=models.CharField(max_length=100)
    def __str__(self):
        return self.n_bastidor

    def get_image_filename(instance, filename):
        id = instance.coche.id
        return "static/img/%s" % (id)  

class FotoCoche(models.Model):
    coche = models.ForeignKey(Coche, on_delete=models.CASCADE)
    fotoCoche = models.ImageField(upload_to='appOutletCar/static/img/coche', default='images/None/no-img.jpg')
    
    def __str__(self):
        return self.coche.n_bastidor+ " Imagen"



class Comment(models.Model):
    coche = models.ForeignKey(Coche,on_delete=models.CASCADE,related_name='comments')
    usuario= models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.usuario)

class TipoDeCoche(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=2000)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username