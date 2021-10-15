from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.


def index(response):
    return HttpResponse("<h1> bagong </h1>")


def v1(response, id):
    ls = ToDoList.objects.get(id=id)
    return HttpResponse("<h1> %s </h1>" % ls.name)


def home(response):
    pass
