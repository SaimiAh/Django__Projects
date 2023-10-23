from django.shortcuts import render
from django.views import generic
def home(request):
    return render(request, 'halls/home.html')
