# Generated by Django 3.2.6 on 2021-08-30 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0024_delete_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='fruit_avg_weight',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Средний вес плода'),
        ),
    ]
