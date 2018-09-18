from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url('movies', views.movielist, name="movielist"),
    url(r'^movie/(?P<id>[0-9]+)/$', views.moviepage, name="moviepage"),
]
