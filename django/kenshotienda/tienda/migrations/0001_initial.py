# Generated by Django 4.1.6 on 2023-03-10 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'categoriaproducto',
                'verbose_name_plural': 'categoriaproductos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='tienda')),
                ('precio', models.FloatField()),
                ('disponibilidad', models.BooleanField(default=True)),
                ('categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.categoriaproducto')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
    ]
