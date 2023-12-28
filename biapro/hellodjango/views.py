from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hellodjango(request):
    return HttpResponse("Hello Django")
