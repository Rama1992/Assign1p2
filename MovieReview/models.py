from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    movieImage = models.CharField(max_length=2000, default="https://p1.hiclipart.com/preview/330/79/764/movie-folder-icons-part-20-interstellar-v1-png-icon.jpg")


class review(models.Model):
    name = models.CharField(max_length=100)
    reviewText = models.TextField(max_length=10000)
    review_date = models.DateTimeField(auto_now_add=True)
    movie_id = models.ForeignKey('movie', default='moviename', on_delete=models.CASCADE)
