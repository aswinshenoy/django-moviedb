from django.shortcuts import render
from . import models

def moviepage(request,id):
    movie = models.movie.objects.get(pk=id)
    return render(request, 'movie/single.html',{'movie':movie})
