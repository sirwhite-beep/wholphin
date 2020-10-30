from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView

from main.models import Comment
from .form import Commentform



def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


def commentview(request):
    comment = Commentform()
    if request.method == 'POST':
        comment = Commentform(request.POST)
        if comment.is_valid():
            comment.save()
            return HttpResponseRedirect(reverse_lazy('met:conconfirm'))
    return render(request, 'main/comment.html', {'com': comment})


def commentconfirm(request):
    return render(request, 'main/commentconfirm.html')


class Commview(ListView):
    model = Comment
    template_name = 'main/commentview.html'
    context_object_name = 'comm'









# Create your views here.
