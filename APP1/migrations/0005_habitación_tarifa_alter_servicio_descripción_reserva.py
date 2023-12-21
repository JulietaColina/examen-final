# Generated by Django 4.2.7 on 2023-11-27 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0004_remove_servicio_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitación',
            name='tarifa',
            field=models.PositiveIntegerField(default=8000),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='descripción',
            field=models.CharField(max_length=50, verbose_name='Descripción'),
        ),
        migrations.CreateModel(
            name='reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant_días', models.PositiveIntegerField()),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='APP1.cliente')),
                ('habitación', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='APP1.habitación')),
            ],
            options={
                'verbose_name': 'reserva',
                'verbose_name_plural': 'Reserva',
                'db_table': 'reserva',
            },
        ),
    ]
