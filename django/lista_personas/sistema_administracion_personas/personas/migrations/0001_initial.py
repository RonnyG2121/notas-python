# Generated by Django 4.2.7 on 2023-11-06 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=30)),
                ('numero', models.IntegerField()),
                ('pais', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=10)),
                ('domicilio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personas.domicilio')),
            ],
        ),
    ]
