"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movies.views import movie_view, TestView, MainView, AboutView, custom_handler404, custom_handler400, \
    custom_handler403, custom_handler500, myview
from job.views import qqq

urlpatterns = [
    path('', MainView.as_view()),
    path('test/', qqq),
    path('about/', AboutView.as_view()),
    path('admin/', admin.site.urls),
    path('movie/<int:movie_id>', movie_view),
    path('imagestore/<int:year>/', myview, name='time-loop'),
    path('imagestore-summary/<int:year>/', myview, {'summary': True}, name='imagestore-summary'),
]

handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500
