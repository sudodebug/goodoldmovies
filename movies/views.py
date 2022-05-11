from django.shortcuts import render
from django.conf import settings
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseServerError

movies = [
    {'title': 'Catchfire', 'year': 1990, },
    {'title': 'Mighty Ducks the Movie: The First Face-Off', 'year': 1997, },
    {'title': 'Le zombie de Cap-Rouge', 'year': 1997, },
]

movie_data = {
    1: 'The dark knight',
    2: '12 Angry men',
    3: 'Il brutto, il cattivo',
}


def movie_view(request, movie_id):
    movie_title = movie_data.get(movie_id)
    return HttpResponse(f'This is {movie_title}')


def custom_handler400(request, exception):
    return HttpResponseBadRequest('Неверный запрос!')


def custom_handler403(request, exception):
    return HttpResponseForbidden('Доступ запрещен!')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')