from django import forms

from .models import Images, Texts, News

class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('title', 'image')
        labels = {'title': 'Название', 'image': 'Ссылка на изображение'}
    

class TextsForm(forms.ModelForm):
	class Meta:
		model = Texts
		fields = ('title', 'text')
		labels = {'title': 'Название', 'text': 'Текст'}


class NewsForm(forms.ModelForm):
	class Meta:
		model = News
		fields = ('title', 'text', 'video', 'image', 'source','author')
		labels = {'title': 'Название', 'text': 'Содержание',
				  'video': 'Ссылка на видео', 'image': 'Ссылка на изображение',
				  'source': 'Источник', 'author': 'Автор'}
		help_texts = {'image': 'Можно добавлять что-то одно из видео или \
							   изображения, если добавишь и то и то будет видно только видео.',
					 'source': 'Не обязательно'}