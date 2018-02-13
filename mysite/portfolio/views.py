from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from portfolio import models


def index(request):
    template = loader.get_template('portfolio/index.html')
    images = models.Image.objects.all()
    context = {
        'images': images
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
