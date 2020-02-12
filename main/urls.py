from django.urls import path

from .views import *

app_name = 'main'
urlpatterns = [
	path('', index, name='index'),
	path('lol/', lol, name='lol'),
	path('news/', NewsView.as_view(), name='news'),
	path('videos/', VideosViews.as_view(), name='videos'),
	path('musics/', MusicsView.as_view(), name='musics'),
	path('images/', ImagesView.as_view(), name='images'),
	path('texts/', TextsView.as_view(), name='texts'),
	path('<str:page>/', other_page, name='other'),
]