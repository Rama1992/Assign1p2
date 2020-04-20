from django.db import models


# Create your models here.
class movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class review(models.Model):
    name = models.CharField(max_length=100)
    reviewText = models.TextField(max_length=10000)
    review_date = models.DateTimeField(auto_now_add=True)
    movie_id = models.ForeignKey('movie', default='moviename', on_delete=models.CASCADE)
