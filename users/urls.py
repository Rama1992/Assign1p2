from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#app_name = 'MovieReview'

urlpatterns = [
    path('register/', views.register, name="users_register"),
    #path('login/', views.login, name="users_login"),
    path('profile/', views.profile, name="users_profile"),
    #path('registration/successful', name='register_done')
    #path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('password_reset_confirm/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]