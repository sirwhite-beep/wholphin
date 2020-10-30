from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from account.forms import Signupform


def signupview(request):
    sign = Signupform()
    if request.method == 'POST':
        sign = Signupform(request.POST)
        if sign.is_valid():
            sign.save()
            return HttpResponseRedirect(reverse_lazy('sign:con'))
    return render(request, 'account/signup.html', {'con': sign})


def confirm(request):
    return render(request, 'account/confirm.html')


# Create your views here.
