from django.urls import path
from Movies.views import movies_list, movie_details

app_name = 'movies'

urlpatterns = [
    path('list/', movies_list, name='movies_list'),
    path('details/<int:pk>/<slug:slug>/', movie_details, name='movie_details'),
]
