from django.urls import path

from .views import *

app_name = 'main'
urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('news/', NewsView.as_view(), name='news'),
	path('news/add/', CreateNewsView.as_view(), name='create_news'),
	path('news/detail/<int:pk>/', NewsDetailView.as_view(), name='detail_news'),
	path('videos/', VideosViews.as_view(), name='videos'),
	path('musics/', MusicsView.as_view(), name='musics'),
	path('images/', ImagesView.as_view(), name='images'),
	path('images/add/', CreateImagesView.as_view(), name='add_images'),
	path('images/detail/<int:pk>/', ImageDetailView.as_view(), name='detail_images'),
	path('texts/', TextsView.as_view(), name='texts'),
	path('texts/detail/<int:pk>/', TextsDetailView.as_view(), name='detail_texts'),
	path('texts/add/', CreateTextsView.as_view(), name='add_texts'),
	path('<str:page>/', other_page, name='other'),
]
