from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    return render(request, 'second_task/index.html')


class ClassRepresentation(TemplateView):
    template_name = 'second_task/class_template.html'


def func_representation(request):
    return render(request, 'second_task/func_template.html')
