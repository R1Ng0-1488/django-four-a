from django import forms

from .models import Images, Texts, News, Comments

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
        fields = '__all__'
        labels = {'title': 'Название', 'text': 'Содержание', 'video': 'Ссылка на видео', 'image': 'Ссылка на изображение', 'source': 'Источник', 'author': 'Автор'}
        help_texts = {'image': 'Можно добавлять что-то одно из видео или изображения, если добавишь и то и то будет видно только видео.', 'source': 'Не обязательно'}

    def clean_video(self):
        val = self.cleaned_data['video']
        if '=' in val:
            sp = val.split('=')
            val = 'https://www.youtube.com/embed/' + sp[-1]
            return val
        return val

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('author', 'content', 'news', 'texts', 'images')
        widgets = {'news': forms.HiddenInput, 'texts': forms.HiddenInput, 'images': forms.HiddenInput}
