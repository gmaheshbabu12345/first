from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def jampandu(request):
    return HttpResponse('<h1>hi jampandu</h1>')
