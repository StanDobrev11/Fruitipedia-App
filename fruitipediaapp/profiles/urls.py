from django.urls import path

from fruitipediaapp.profiles.views import create_profile, edit_profile, delete_profile, details_profile

urlpatterns = [
    path('create/', create_profile, name='create profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),
    path('details/', details_profile, name='details profile'),
]