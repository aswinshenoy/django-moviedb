from django.db import models
from django.contrib import admin
from django.utils import timezone

class artist(models.Model):
    name = models.CharField(max_length=200, verbose_name='ARTIST')
    imdb_id = models.CharField(max_length=30, verbose_name='IMDB ID')

    class meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"

    def __str__(self):
        return self.name

class movie(models.Model):
    imdb_id = models.CharField(max_length=30,verbose_name='IMDB ID')
    title = models.CharField(max_length=100,verbose_name='MOVIE NAME')
    director = models.ForeignKey(artist, on_delete=models.CASCADE, verbose_name='DIRECTOR')
    artists = models.ManyToManyField(artist, related_name = 'actor', through='roles', verbose_name='ACTORS/ACTRESS IN THIS MOVIE')

    class meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.title

class roles(models.Model):
    role_name = models.CharField(max_length=100,verbose_name='ROLE OF ACTOR IN MOVIE')
    artist = models.ForeignKey(artist, on_delete=models.CASCADE, verbose_name='SELECT ARTIST PROFILE')
    movie = models.ForeignKey(movie, on_delete=models.CASCADE, verbose_name='SELECT MOVIE PROFILE')

    class meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.role_name

class roles_inline(admin.TabularInline):
    model = roles
    extra = 1

class artistAdmin(admin.ModelAdmin):
    inlines = (roles_inline,)

class movieAdmin(admin.ModelAdmin):
    inlines = (roles_inline,)
