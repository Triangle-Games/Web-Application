# Generated by Django 3.2.5 on 2021-07-20 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0002_auto_20210720_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.CharField(max_length=255, verbose_name='Применяетсяя к странице'),
        ),
    ]