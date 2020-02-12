from django.shortcuts import render

class ObjectsMixin:
	model = None
	template = None

	def get(self, request):
		obj = self.model.objects.all()
		return render(request, self.template, {self.model.__name__.lower(): obj})