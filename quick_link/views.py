from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from quick_link.models import Enrol
from .form import Complaintform, Enrolform, Enroldetailform


def complainttview(request):
    complaint = Complaintform()
    if request.method == 'POST':
        complaint = Complaintform(request.POST)
        if complaint.is_valid():
            complaint.save()
            return HttpResponseRedirect(reverse_lazy('quick:complaint2'))
    return render(request, 'quick/complaint.html', {'comp': complaint})


def enrolview(request):
    enroll = Enrolform()
    if request.method == 'POST':
        enroll = Enrolform(request.POST)
        if enroll.is_valid():
            enroll.save()
            return HttpResponseRedirect(reverse_lazy('quick:detail'))
    return render(request, 'quick/enrol.html', {'empty': enroll})


def enroldetailview(request):
    enroll = Enroldetailform()
    if request.method == 'POST':
        enroll = Enroldetailform(request.POST)
        if enroll.is_valid():
            enroll.save()
            return HttpResponseRedirect(reverse_lazy('quick:end'))
    return render(request, 'quick/enroldetail.html', {'empty': enroll})


def confirm(request):
    return render(request, 'quick/confirm.html')


class Complaint2(ListView):
    template_name = 'quick/complaint2.html'
    queryset = 'all'


def pay(request):
    return render(request, 'quick/payment.html')


def enrol(request):
    return render(request, 'quick/enrol.html')


class Enroll(ListView):
    model = Enrol
    context_object_name = 'end'
    template_name = 'quick/enrolment.html'


class Enrolldetail(DetailView):
    model = Enrol
    context_object_name = 'detail'
    template_name = 'quick/enrolmentdetail.html'


class Enrolprint(ListView):
    template_name = 'quick/enrolprint.html'
    queryset = 'all'

