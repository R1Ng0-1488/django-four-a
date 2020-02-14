from django.shortcuts import render
from django.core.paginator import Paginator

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