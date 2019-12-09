# Generated by Django 2.2.6 on 2019-12-09 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_bastidor', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('anyo', models.IntegerField()),
                ('n_km', models.IntegerField()),
                ('combustible', models.CharField(max_length=100)),
                ('potencia', models.IntegerField()),
                ('precio', models.FloatField()),
                ('cambio', models.CharField(max_length=100)),
                ('consumo', models.FloatField()),
                ('comentario', models.CharField(max_length=1000)),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('cod_ciudad', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('ciudad', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('nombre_Marca', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=5000)),
                ('fecha_creacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeCoche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=2000)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('correo', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('contrasenya', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_site', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('nombre_Modelo', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=100)),
                ('traccion', models.IntegerField()),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appOutletCar.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='FotoCoche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotoCoche', models.ImageField(default='images/None/no-img.jpg', upload_to='appOutletCar/static/img/coche')),
                ('coche', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appOutletCar.Coche')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('coche', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='appOutletCar.Coche')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.AddField(
            model_name='coche',
            name='lugar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appOutletCar.Lugar'),
        ),
        migrations.AddField(
            model_name='coche',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appOutletCar.Modelo'),
        ),
        migrations.AddField(
            model_name='coche',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
