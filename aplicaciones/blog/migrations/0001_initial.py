# Generated by Django 4.0.4 on 2022-06-08 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('estado', models.BooleanField(default=True, verbose_name='Autor Activo/No activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=255)),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]