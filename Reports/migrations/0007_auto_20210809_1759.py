# Generated by Django 3.2.5 on 2021-08-09 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0006_auto_20210803_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='measurement_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата замера'),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_comment',
            field=models.CharField(blank=True, max_length=255, verbose_name='Комментарий к отчету'),
        ),
    ]
