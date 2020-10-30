from django.shortcuts import render


def emma(request):
    return render(request, 'student_info/emma.html')


def christy(request):
    return render(request, 'student_info/christy.html')


def rob(request):
    return render(request, 'student_info/rob.html')


def imoh(request):
    return render(request, 'student_info/imoh.html')

# Create your views here.
