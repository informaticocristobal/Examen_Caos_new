# Generated by Django 4.2.1 on 2023-07-04 04:34

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
            name='Categoria',
            fields=[
                ('categoria', models.CharField(max_length=60, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('correo', models.CharField(max_length=45)),
                ('fono', models.IntegerField()),
                ('mensaje', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='objcarrito',
            fields=[
                ('idobjeto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_objeto', models.CharField(max_length=60)),
                ('precio', models.IntegerField()),
                ('foto', models.ImageField(default='fotos/default.png', null=True, upload_to='fotos')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('idnoticia', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_periodista', models.CharField(max_length=60)),
                ('titulo_noticia', models.CharField(default='--', max_length=300)),
                ('titular_noticia', models.CharField(default='--', max_length=300)),
                ('cuerpo_noticia', models.CharField(default='--', max_length=300)),
                ('foto', models.ImageField(default='fotos/defaut.png', null=True, upload_to='fotos')),
                ('publicar', models.BooleanField(default=False)),
                ('comentario', models.CharField(default='S/C', max_length=45)),
                ('precio', models.IntegerField(default=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webCaosNew.categoria')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('idGaleria', models.AutoField(primary_key=True, serialize=False)),
                ('foto', models.ImageField(upload_to='fotos')),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webCaosNew.noticia')),
            ],
        ),
    ]
