from django.urls import path
from . import views

#app_name = 'MovieReview'

urlpatterns = [
    #path('', views.home, name="MovieReview_home"),
    path('', views.cinemas, name="cinemas"),
    path("<int:pk>/", views.cinema_detail, name="cinema_detail"),
    path('cinemas/', views.cinemas, name ="cinemas"),
    path('review/<int:pk>/edit/', views.review_edit, name='review_edit')
]