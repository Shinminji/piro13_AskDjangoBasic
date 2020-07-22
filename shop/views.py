from django.http import HttpResponse
from django.shortcuts import render

#view 호출에 대한 리턴값은 HttpResponse객체


def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))
