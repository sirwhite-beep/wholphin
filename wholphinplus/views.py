from django.shortcuts import render
from django.views.generic import TemplateView

'''
def payment(request):
    return render(request, 'payment.html')
'''


class Payment(TemplateView):
    template_name = 'payment.html'


def main(request):
    return render(request, 'main.html')


def index(request):
    return render(request, 'index.html')


class Read(TemplateView):
    template_name = 'readmore.html'


class Rea(TemplateView):
    template_name = 'read.html'


class Read1(TemplateView):
    template_name = 'read1.html'


class Event(TemplateView):
    template_name = 'event.html'


class Allnews(TemplateView):
    template_name = 'readnews.html'


class Navbar(TemplateView):
    template_name = 'navbar.html'

