from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


def home_view(request):
    """
    Домашняя страница, главная
    :param request: Запрос пользователя
    :return: Доступные страницы
    """
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    """
    Вывод текущего времени
    :param request: Запрос пользователя
    :return: Текущее время
    """
    current_time = datetime.now()
    msg = f'Текущее время: {current_time.time()}'
    return HttpResponse(msg)


def workdir_view(request):
    """
    Вывод текщей рабочей директории
    :param request: Запрос пользователя
    :return: Список рабочей директории
    """
    direct = os.listdir()
    return HttpResponse(direct)


