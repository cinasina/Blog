from django.shortcuts import render, get_list_or_404
from Movies.models import Movies


def movies_list(request):
    movies = Movies.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/movies_list.html', context=context)


def movie_details(request, pk, slug):
    details = get_list_or_404(Movies, pk=pk, slug=slug)
    context = {'details': details}
    return render(request, 'movies/movie_details.html', context=context)
