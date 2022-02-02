from django.shortcuts import render
from . models import Genre

# Create your views here.

def index(request):

    genres = Genre.objects.all()
    gen = list(Genre.objects.values())

    context = {'genres': genres, 'gen':gen}

    return render(request, "base/index.html", context)


