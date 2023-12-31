# Generated by Django 4.2.7 on 2023-11-27 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0002_rename_genero_cliente_género'),
    ]

    operations = [
        migrations.CreateModel(
            name='servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20, verbose_name='Tipo')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('tarifa', models.CharField(max_length=20, verbose_name='Tarifa')),
                ('descripción', models.CharField(max_length=20, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'Servicios',
                'db_table': 'servicio',
            },
        ),
        migrations.CreateModel(
            name='habitación',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('S', 'Suite'), ('M', 'Matrimonial'), ('I', 'Individual')], max_length=1)),
                ('servicios', models.ManyToManyField(to='APP1.servicio')),
            ],
            options={
                'verbose_name': 'habitación',
                'verbose_name_plural': 'Habitaciones',
                'db_table': 'habitación',
            },
        ),
    ]
