# Generated by Django 4.0.4 on 2022-07-03 14:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]