from django.shortcuts import render
from django.http import HttpResponse
# def home(request):
#     return HttpResponse("Welcome to my To-Do List App")
def home(request):
    return render(request,'tasks/home.html')