from datetime import timezone

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from MovieReview.forms import ReviewForm
from MovieReview.models import movie, review
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (UpdateView)


def cinemas(request):
    movie_list = movie.objects.all()
    context = {
        'movies': movie_list,
    }
    return render(request, 'movies.html', context)

@login_required()
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

def review_edit(request, pk):
    rev = get_object_or_404(review, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('cinema_detail', pk=post.pk)
    else:
        form = ReviewForm(instance=rev)
    return render(request, 'review_edit.html', {'form': form})





