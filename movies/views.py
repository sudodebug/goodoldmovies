from django.shortcuts import render
from django.conf import settings
from django.views import View

movies = [
    {'title': 'Catchfire', 'year': 1990, },
    {'title': 'Mighty Ducks the Movie: The First Face-Off', 'year': 1997, },
    {'title': 'Le zombie de Cap-Rouge', 'year': 1997, },
    ]


def movie_view(request):
    context = {'movies': movies}
    return render(request, 'movies/index.html', context=context)

