from django.contrib import admin
from MovieReview.models import movie, review


class PostMovie(admin.ModelAdmin):
    pass


class PostReview(admin.ModelAdmin):
    pass


admin.site.register(movie, PostMovie)
admin.site.register(review, PostReview)
