# Generated by Django 4.1 on 2022-09-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_order_quantity_remove_order_taste_orderdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='singlepod',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9),
            preserve_default=False,
        ),
    ]
