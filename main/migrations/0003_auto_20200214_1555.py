# Generated by Django 3.0.2 on 2020-02-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200214_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(max_length=200, verbose_name='Автор'),
        ),
    ]
