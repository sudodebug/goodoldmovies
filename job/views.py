from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views import View


def qqq(request):
    return render(request, 'job/test.html')
