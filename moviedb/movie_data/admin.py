from django.contrib import admin
from .models import movie, artist, roles, artistAdmin, movieAdmin

admin.site.register(movie, movieAdmin)
admin.site.register(artist, artistAdmin)
admin.site.register(roles)
