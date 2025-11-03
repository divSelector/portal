from django.shortcuts import render

from links.data import data

def index(request):
    return render(request, 'render/index.html', {'nodes': data})