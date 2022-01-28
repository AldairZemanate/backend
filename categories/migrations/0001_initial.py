# Generated by Django 3.2.10 on 2022-01-28 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0005_auto_20220128_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='cat_name', max_length=64, verbose_name='nombre')),
                ('description', models.CharField(blank=True, db_column='cat_description', max_length=254, null=True, verbose_name='descripcion')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='fecha de actualización')),
                ('products', models.ManyToManyField(to='products.Product', verbose_name='productos')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category', verbose_name='categoria')),
                ('pro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='productos')),
            ],
            options={
                'verbose_name': 'categoria/producto ',
                'verbose_name_plural': 'categorias/productos',
            },
        ),
    ]
