# Generated by Django 4.2.7 on 2023-11-27 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0005_habitación_tarifa_alter_servicio_descripción_reserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.PositiveIntegerField()),
                ('forma_pago', models.CharField(choices=[('V', 'Varón'), ('M', 'Mujer')], max_length=1)),
                ('fecha_pago', models.DateField()),
                ('reserva', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='APP1.reserva')),
            ],
            options={
                'verbose_name': 'pago',
                'verbose_name_plural': 'Pagos',
                'db_table': 'pago',
            },
        ),
    ]
