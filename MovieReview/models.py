from django.db import models


# Create your models here.
class movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)
