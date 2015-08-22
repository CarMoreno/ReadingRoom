# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, verbose_name=b'e-mail', blank=True)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('domicilio', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=60)),
                ('estado', models.CharField(max_length=30)),
                ('pais', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Editores',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField(help_text=b'Usa el formato DD/MMM/YYYY')),
                ('portada', models.ImageField(upload_to=b'portadas/')),
                ('sinopsis', models.TextField(blank=True)),
                ('autores', models.ManyToManyField(to='biblioteca.Autor')),
                ('editor', models.ForeignKey(to='biblioteca.Editor')),
            ],
        ),
    ]
