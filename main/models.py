from django.db import models
from django.contrib.auth.models import User

from embed_video.fields import EmbedVideoField
# Create your models here.

class News(models.Model):
	title = models.CharField(max_length=200,
								 verbose_name='Заголовок')
	text = models.TextField(verbose_name='Описание')
	video = EmbedVideoField(blank=True, verbose_name='Видео')
	# image = models.ImageField(blank=True, upload_to='media',
	# 						  verbose_name='Изображение')
	image = models.URLField(blank=True, null=True, verbose_name='Изображение')
	author = models.ForeignKey(User, on_delete=models.PROTECT,
							   verbose_name='Автор')
	published = models.DateTimeField(auto_now_add=True,
									 verbose_name='Опубликовано')	


	class Meta:
		verbose_name = 'Новости'
		verbose_name_plural = 'Новости'
		ordering = ['-published']

	def __str__(self):
		return self.title


class Videos(models.Model):
	title = models.CharField(max_length=200,
							 verbose_name='Название')
	video = EmbedVideoField(verbose_name='Видео')
	published = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
	rubric = models.ForeignKey('Rubrics', on_delete=models.PROTECT,
							   verbose_name='Рубрика')

	class Meta:
		verbose_name = 'Видео'
		verbose_name_plural = 'Видео'

	def __str__(self):
		return self.title


class Rubrics(models.Model):
	name = models.CharField(max_length=200, 
							verbose_name='Название')

	class Meta:
		verbose_name = 'Рубрика'
		verbose_name_plural = 'Рубрики'

	def __str__(self):
		return self.name


class Musics(models.Model):
	title = models.CharField(max_length=200, verbose_name='Название')
	# music = models.FileField(upload_to='audio', verbose_name='Музыка')
	music = models.URLField(verbose_name='Музыка')
	# image = models.ImageField(blank=True, upload_to='media', verbose_name='Изображение')
	image = models.URLField(blank=True, verbose_name='Изображение', null=True)
	published = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
	album = models.ForeignKey('Albums', verbose_name='Альбом', 
							  on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Музыка'
		verbose_name_plural = 'Музыки'

	def __str__(self):
		return self.title


class Albums(models.Model):
	title = models.CharField(max_length=200, verbose_name='Альбом')
	text = models.TextField(verbose_name='Описание')
	# image = models.ImageField(upload_to='media', blank=True,
	# 						  verbose_name='Изображение')
	image = models.URLField(blank=True, null=True, verbose_name='Изображение')
	published = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

	class Meta:
		verbose_name = 'Альбом'
		verbose_name_plural = 'Альбомы'
		ordering = ['-published']
			
	def __str__(self):
		return self.title


class Images(models.Model):
	title = models.CharField(max_length=200, verbose_name='Название', 
							 blank=True)
	# image = models.ImageField(upload_to='media', verbose_name='Изображение')
	image = models.URLField(verbose_name='Изображение')
	published = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

	class Meta:
		verbose_name = 'Фото'
		verbose_name_plural = 'Фото'
		ordering = ['-published']

	def __str__(self):
		return self.title	


class Texts(models.Model):
	title = models.CharField(max_length=200, verbose_name='Название')
	text = models.TextField(verbose_name='Текст')
	published = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

	class Meta:
		verbose_name = 'Текст'
		verbose_name_plural = 'Текста'
		ordering = ['-published']

	def __str__(self):
		return self.title


