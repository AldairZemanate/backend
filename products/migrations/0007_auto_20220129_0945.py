# Generated by Django 3.2.10 on 2022-01-29 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.PositiveIntegerField(db_column='prod_amount', verbose_name='cantidad'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveSmallIntegerField(blank=True, db_column='prod_discount', default=0, null=True, verbose_name='descuento'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(db_column='prod_price', verbose_name='precio'),
        ),
    ]
