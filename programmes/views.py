from django.shortcuts import render
from django.views.generic import ListView, TemplateView


def web(request):
    return render(request, 'programmes/web.html')


class App(ListView):
    template_name = 'programmes/app.html'
    queryset = 'all'


class Machine(ListView):
    template_name = 'programmes/machine.html'
    queryset = 'all'


class Data(ListView):
    template_name = 'programmes/data.html'
    queryset = 'all'


class Generic(ListView):
    template_name = 'programmes/generic.html'
    queryset = 'all'


class Graphic(ListView):
    template_name = 'programmes/graphic.html'
    queryset = 'all'


class Software(ListView):
    template_name = 'programmes/software.html'
    queryset = 'all'




# Create your views here.
