from django.shortcuts import render


# Create your views here.

def index(request):
    template = 'index.html'
    context = {}
    return render(request, template, context)


def not_found(request):
    template = '404.html'
    context = {}
    return render(request, template, context)