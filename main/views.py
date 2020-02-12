from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import View
from django.template import TemplateDoesNotExist
from django.template.loader import get_template

from .models import *
from .utils import ObjectsMixin
# Create your views here.


class NewsView(ObjectsMixin, View):
	model = News
	template = 'main/news.html'


class VideosViews(ObjectsMixin, View):
	model = Rubrics
	template = 'main/videos.html'


class MusicsView(ObjectsMixin, View):
	model = Albums
	template = 'main/musics.html'
	

class ImagesView(ObjectsMixin, View):
	model = Images
	template = 'main/images.html'


class TextsView(ObjectsMixin, View):
	model = Texts
	template = 'main/texts.html'


def other_page(request, page):
	try:
		template = get_template('main/' + page + '.html')
	except TemplateDoesNotExist:
		raise Http404
	return HttpResponse(template.render(request=request))

def lol(request):
	return render(request, 'main/lol.html')

def index(request):
	return render(request, 'main/index.html')