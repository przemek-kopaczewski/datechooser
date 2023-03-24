from django.shortcuts import render


def index(request):
    return render(request, 'datechooser/base.html')


def create_event(request):
    return render(request, 'datechooser/create_event.html')
