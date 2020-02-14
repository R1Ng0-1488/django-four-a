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
	image = forms.URLField(label='Ссылка на изображение', help_text='Можно добавлять что-то одно из \
		видео или изображения, если добавишь и то и то будет видно только видео.')
	source = forms.URLField(label='Источник', help_text='Не обязательно')
	class Meta:
		model = News
		fields = ('title', 'text', 'video', 'image', 'source','author')
		labels = {'title': 'Название', 'text': 'Содержание',
				  'video': 'Ссылка на видео', 'author': 'Автор'}