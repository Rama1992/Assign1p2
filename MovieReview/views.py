from django.shortcuts import render
from django.http import HttpResponse
from MovieReview.models import movie, review


def cinemas(request):
    movie_list = movie.objects.all()
    context = {
        'movies': movie_list,
    }
    return render(request, 'movies.html', context)

