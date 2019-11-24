from django.contrib import admin

from .models import Marca, Modelo, Coche, Usuario, Lugar, Comment, FotoCoche 
# Register your models here.

class LugarAdmin(admin.ModelAdmin):
    list_display = ('cod_ciudad', 'ciudad', 'provincia')
    search_fields = ['nombre', 'content']
  
admin.site.register(Lugar, LugarAdmin)

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre_Marca', 'descripcion', 'fecha_creacion')
    search_fields = ['nombre', 'content']
  
admin.site.register(Marca, MarcaAdmin)

class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nombre_Modelo', 'categoria', 'traccion', 'marca')
    search_fields = ['nombre', 'content']
  
admin.site.register(Modelo, ModeloAdmin)

class CocheAdmin(admin.ModelAdmin):
    list_display = ('n_bastidor', 'estado', 'color', 'anyo', 'n_km', 'combustible', 'potencia', 'precio', 'cambio', 'consumo', 'comentario', 'modelo', 'lugar')
    search_fields = ['bastidor', 'content']
    prepopulated_fields = {'slug': ('n_bastidor',)}
admin.site.register(Coche, CocheAdmin)

class fotoCocheAdmin(admin.ModelAdmin):
    list_display = ('coche', 'fotoCoche')
    search_fields = ['coche', 'content']
admin.site.register(FotoCoche, fotoCocheAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('correo', 'nombre_usuario', 'apellidos', 'telefono', 'contrasenya', 'coche')
    search_fields = ['nombre', 'content']
  
admin.site.register(Usuario, UsuarioAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'coche', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
admin.site.register(Comment, CommentAdmin)