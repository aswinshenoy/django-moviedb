from django.shortcuts import render
from . import models

def moviepage(request,id):
    movie = models.movie.objects.get(pk=id)
    return render(request, 'movie/single.html',{'movie':movie})

def movielist(request):
     movies = models.movie.objects.all()
     return render(request, 'movie/list.html', {'movies': movies})
