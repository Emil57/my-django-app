import datetime
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to meeting planner")

def date(request):
    return HttpResponse("The server was called at: " + str(datetime.datetime.now()))

def about(request):
    return HttpResponse("I am Dimas and I do web apps with Django.")
