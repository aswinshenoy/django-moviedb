from django.shortcuts import render
from . import models

def moviepage(request,id):
    movie = models.movie.objects.get(pk=id)
    return render(request, 'movie/single.html',{'movie':movie})

def movielist(request):
     movies = models.movie.objects.all()
     return render(request, 'movie/list.html', {'movies': movies})

def artistpage(request,id):
    artist = models.artist.objects.get(pk=id)
    return render(request, 'artist/single.html',{'artist':artist})

def artistlist(request):
     artists = models.artist.objects.all()
     return render(request, 'artist/list.html', {'artists': artists})
