from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def men(request):
    template = loader.get_template('men.html')
    return HttpResponse(template.render())


def women(request):
    return render(request, 'women.html')


def kids(request):
    return render(request, 'kids.html')


def tailors(request):
    return render(request, 'tailors.html')


def team(request):
    return render(request, 'team.html')


def login(request):
    return render(request, 'login.html')
