from django.urls import path
from django.urls.resolvers import URLPattern
from django.views.generic.base import View
from .views import ActorListView, MovieListView, Actor_MoviesListView

urlpatterns = [
    path("actor", ActorListView.as_view()),
    path("movie", MovieListView.as_view()),
    path("actor_movie", Actor_MoviesListView.as_view())
]