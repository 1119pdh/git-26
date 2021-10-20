import json

from django.db.models.fields import EmailField
from django.http import HttpResponse, JsonResponse, request
from django.views import View
from django.shortcuts import render

from .models import Actor, Actor_movie
from moviestar.models import Movie

# Create your views here.

class ActorListView(View):
    def post(self, request):
        data= json.loads(request.body)

        Actor.objects.create(
            first_name = data["first_name"],
            last_name = data["last_name"],
            date_of_birth = data["date_of_birth"]
        )
        return JsonResponse({"message" : "SUCCESS"}, status= 201)

    def get(self, request):
        results = []

        actors = Actor.objects.all()
        for actor in actors:
            actors_movies = Actor_movie.objects.filter(actor_id=actor.id)
            movie_list= []
            for actor_movie in actors_movies:
                  movie_list.append(
                       {
                       "id"    : actor_movie.movie.id, 
                       "title" : actor_movie.movie.title
                       }
                  )
            results.append(
                  {
                      "first_name" : actor.first_name, 
                      "last_name" : actor.last_name,
                      "movie" : movie_list         
                  }
            )
        return JsonResponse({"actors" : results}, status= 200)          



class MovieListView(View):
    def post(self,request):
        data= json.loads(request.body)
        
        Movie.objects.create(
            title = data["title"],
            release_date = data["release_date"],
            running_time = data["running_time"]
        )

        return JsonResponse({"message" : "SUCCESS"}, status= 201)

    def get(self,request):
        results=[]

        movies = Movie.objects.all()
        
        actor_list=[]
        for movie in movies:
            actors = movie.actor_movie.actor_set.all()
            actor_list=[]
            for actor in actors:
                actor_list.append(
                    {
                    "name" : actor.first_name + actor.last_name
                    }   
                )
        results.append(
            {
                "title" : movie.title ,
                "release_date" : movie.releas_date
            }
        )
        return JsonResponse({"movies" : results}, status= 200)

class Actor_MoviesListView(View):
    def post(self,request):
        data= json.loads(request.body)

        Actor_movie.objects.create(
            actor= Actor.objects.get(last_name = data["actor_id"]),
            movie= Movie.objects.get(title = data["movie_id"])
        )

        return JsonResponse({"message" : "SUCCESS"}, status= 201)