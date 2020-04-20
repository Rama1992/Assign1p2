from django.urls import path
from . import views

#app_name = 'MovieReview'

urlpatterns = [
    path("", views.cinemas, name="cinemas"),
    #path("<int:pk>/", views.cinema_detail, name='cinemas_detail')
]