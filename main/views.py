from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import *
from .utils import ObjectsMixin, ObjectDetailView
from .forms import *
# Create your views here.


class NewsView(ObjectsMixin, View):
	model = News
	template = 'main/news.html'


class NewsDetailView(ObjectDetailView):
	model = News
	template_name = 'main/news_detail.html'
	success_url = '/news/detail/{news_id}'


class VideosViews(ObjectsMixin, View):
	model = Rubrics
	template = 'main/videos.html'


class MusicsView(ObjectsMixin, View):
	model = Albums
	template = 'main/musics.html'


class ImagesView(ObjectsMixin, View):
	model = Images
	template = 'main/images.html'


class ImageDetailView(ObjectDetailView):
	model = Images
	template_name = 'main/images_detail.html'
	success_url = '/images/detail/{images_id}'


class TextsView(ObjectsMixin, View):
	model = Texts
	template = 'main/texts.html'


class TextsDetailView(ObjectDetailView):
	model = Texts
	template_name = 'main/texts_detail.html'
	success_url = '/texts/detail/{texts_id}'

class IndexView(TemplateView):
	template_name = 'main/index.html'


class CreateImagesView(LoginRequiredMixin, CreateView):
	template_name = 'main/create_images.html'
	form_class = ImagesForm
	success_url = reverse_lazy('main:images')


class CreateTextsView(LoginRequiredMixin, CreateView):
	template_name = 'main/create_texts.html'
	form_class = TextsForm
	success_url = reverse_lazy('main:texts')


class CreateNewsView(LoginRequiredMixin, CreateView):
	template_name = 'main/create_news.html'
	form_class = NewsForm
	success_url = reverse_lazy('main:news')




def other_page(request, page):
	try:
		template = get_template('main/' + page + '.html')
	except TemplateDoesNotExist:
		raise Http404
	return HttpResponse(template.render(request=request))
