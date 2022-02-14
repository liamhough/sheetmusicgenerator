from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse


def index(request):
    template = loader.get_template('home.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))


def composition(request):
    template = loader.get_template('composition.html')
    name = request.GET['name']
    context = {
        "name": name
    }
    return HttpResponse(template.render(context, request))

def recording(request):
    template = loader.get_template('recording.html')
    name = request.GET['name']
    context = {
        "name": name
    }
    return HttpResponse(template.render(context, request)) 