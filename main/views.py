from django.shortcuts import render, HttpResponse
from .models import ToDo


def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})


def second(request):
    return HttpResponse("test 2 page")



def third(request):
    return HttpResponse("This is page test 3!")


def add(request):
    return render(request, "addindex.html")

def change(request):
    return render(request, "changeindex.html")

def delete(request):
    return render(request, "deleteindex.html")

