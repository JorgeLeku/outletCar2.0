# Generated by Django 3.0 on 2019-12-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOutletCar', '0003_auto_20191124_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDeCoche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='fotocoche',
            name='fotoCoche',
            field=models.ImageField(default='images/None/no-img.jpg', upload_to='appOutletCar/static/img/coche'),
        ),
    ]
