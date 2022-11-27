# Generated by Django 4.1 on 2022-11-27 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TecnicoMaster',
            fields=[
                ('usuarioTecnico', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombreTecnico', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usuarioUsuario', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombreUsuario', models.CharField(max_length=20)),
            ],
        ),
    ]