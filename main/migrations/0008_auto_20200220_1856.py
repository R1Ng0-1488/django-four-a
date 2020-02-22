# Generated by Django 3.0.3 on 2020-02-20 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_delete_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Images', verbose_name='Фотки')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.News', verbose_name='Новости')),
                ('texts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Texts', verbose_name='Текста')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Коментарии',
                'ordering': ['-published'],
            },
        ),
    ]