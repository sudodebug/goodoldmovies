from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseServerError, HttpResponseRedirect


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


class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'movies/test.html', {})


class AboutView(View):
    def get(self, request):
        return render(request, 'movies/about.html', {})


class MainView(View):
    def get(self, request):
        return render(request, 'movies/movieindex.html')


def custom_handler400(request, exception):
    return HttpResponseBadRequest('Неверный запрос!')


def custom_handler403(request, exception):
    return HttpResponseForbidden('Доступ запрещен!')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')


def myview(request, year, **kwargs):
    year = int(year)
    summary = kwargs.get('summary', False)

    if year < 1900:
        return HttpResponseRedirect(reverse('time-loop', args=[2000]))
    elif year > 2000:
        return HttpResponseRedirect(reverse('time-loop', args=[1900]))
    else:
        return render(request, 'movies/browser.html', {'year': year, 'summary': summary})