from django.utils import timezone
from django.db import models

from django.db.models.deletion import CASCADE

class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField(default=timezone.now)

    class Meta:
        db_table = 'actors'

class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField(default=timezone.now)
    running_time = models.IntegerField()

    class Meta:
        db_table = 'movies'

class Actor_movie(models.Model):
    actor = models.ForeignKey('actor', on_delete=models.CASCADE)
    movie = models.ForeignKey('movie', on_delete=models.CASCADE)

    class Meta:
        db_table = 'actor_movies'