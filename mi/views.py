from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def rohith(request):
    return HttpResponse('<h1>mi team captain is Rohith</h1>')
