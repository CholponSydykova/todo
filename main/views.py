from django.shortcuts import render, HttpResponse
from .models import ToDo
from .models import Book


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

def books(request): 
    books = Book.objects.all()
<<<<<<< HEAD
    return render(request, "books.html" , {"books" : books})
=======
    return render(request, "books.html" , {"books" : books})

>>>>>>> ae1ac2a66968e4b0c6fb4d4c9c93e716aa478c95
