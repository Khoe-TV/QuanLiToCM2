from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    response = HttpResponse()
    response.writelines('<h1>Le Thanh Khoe</h1>')
    response.write('Day la app Home')
    response.write('<h2>Second update</h2>')
    response.write('<h2>Third update</h2>')
    return response
