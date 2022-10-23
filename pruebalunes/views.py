import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.http import HttpResponse

from .models import Country
from .serializers import CountrySerializer


def view_damehora(request):
    now = datetime.datetime.now()
    html = "<html><body> Son las %s.</body><html>" % now
    return HttpResponse(html)


def view_helloworld(request, name):
    html = "<html><body> Hola %s ,Bienvenido.</body><html>" % name
    return HttpResponse(html)


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
