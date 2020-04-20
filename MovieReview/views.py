from django.shortcuts import render
from django.http import HttpResponse
from MovieReview.models import movie, review


def cinemas(request):
    movie_list = movie.objects.all()
    context = {
        'movies': movie_list,
    }
    return render(request, 'movies.html', context)


def cinema_detail(request, pk):
    movieId = movie.objects.get(pk=pk)
    context = {
        "movie": movieId,
    }
    return render(request, "movie.html", context)

