from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from .models import *
from .forms import CommentsForm

class ObjectsMixin:
	model = None
	template = None

	def get(self, request):
		obj = self.model.objects.all()
		paginator = Paginator(obj, 10)
		if 'page' in request.GET:
			page_num = request.GET['page']
		else:
			page_num = 1
		page = paginator.get_page(page_num)
		context = {self.model.__name__.lower(): page.object_list, 'page': page}
		return render(request, self.template, context)


class ObjectDetailView(LoginRequiredMixin, CreateView):
	model = None
	form_class = CommentsForm
	template_name = None
	success_url = None
	initial = {}

	def get_initial(self, *args, **kwargs):
		initial = super().get_initial(*args, **kwargs)
		initial[self.model.__name__.lower()] = get_object_or_404(self.model, pk=self.kwargs['pk'])
		return initial

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context[self.model.__name__.lower()] = get_object_or_404(self.model, pk=self.kwargs['pk'])
		if self.model == Images:
			context['comments'] = Comments.objects.filter(images=context[self.model.__name__.lower()].pk)
		elif self.model == News:
			context['comments'] = Comments.objects.filter(news=context[self.model.__name__.lower()].pk)
		elif self.model == Texts:
			context['comments'] = Comments.objects.filter(texts=context[self.model.__name__.lower()].pk)
		return context
