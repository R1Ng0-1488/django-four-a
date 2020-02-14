from django.urls import path

from .views import *

app_name = 'main'
urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('news/', NewsView.as_view(), name='news'),
	path('add_news/', CreateNewsView.as_view(), name='create_news'),
	path('videos/', VideosViews.as_view(), name='videos'),
	path('musics/', MusicsView.as_view(), name='musics'),
	path('images/', ImagesView.as_view(), name='images'),
	path('add_images/', CreateImagesView.as_view(), name='add_images'),
	path('texts/', TextsView.as_view(), name='texts'),
	path('add_texts/', CreateTextsView.as_view(), name='add_texts'),
	path('<str:page>/', other_page, name='other'),
]