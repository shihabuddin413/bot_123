from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html', {'name': 'shihab'})


def add(request):
    val = request.GET['calcExp']
    res = eval(val)
    if (not res):
        res = "There is an error with expression"
    return render(request, 'result.html', {'expression': val, 'result': res})
