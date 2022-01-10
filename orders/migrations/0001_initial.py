# Generated by Django 3.2.10 on 2022-01-06 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ord_state', models.CharField(choices=[('CONFIRMED', 'confirmado'), ('UNCONFIRMED', 'confirmado'), ('CANCELLED', 'cancelado'), ('DISPATCHED', 'despachado'), ('DELIVERED', 'entregado')], max_length=15, verbose_name='estado')),
                ('ord_total', models.IntegerField(verbose_name='total')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'verbose_name': 'pedido',
                'verbose_name_plural': 'pedidos',
            },
        ),
    ]
