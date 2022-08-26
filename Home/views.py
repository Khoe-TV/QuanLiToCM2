from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    response = HttpResponse()
    response.writelines('<h1>Le Thanh Khoe</h1>')
    response.write('Day la app Home')
    return response
