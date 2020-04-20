from django.http import HttpResponseRedirect
from django.shortcuts import render
from MovieReview.forms import ReviewForm
from MovieReview.models import movie, review


def cinemas(request):
    movie_list = movie.objects.all()
    context = {
        'movies': movie_list,
    }
    return render(request, 'movies.html', context)


def cinema_detail(request, pk):
    movieId = movie.objects.get(pk=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviewData = review(
                name=form.cleaned_data["name"],
                reviewText=form.cleaned_data["reviewText"],
                movie_id=movie.objects.get(pk=pk)
            )
            reviewData.save()
            return HttpResponseRedirect('#')

    reviews = review.objects.filter(movie_id=movieId)
    context = {
        "movie": movieId,
        "reviews": reviews,
        "form": form,
    }
    return render(request, "movie.html", context)
