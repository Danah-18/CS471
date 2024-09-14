from django.shortcuts import render
from django.shortcuts import render 
from django.http import HttpResponse

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html" , {"name": name})    


def index2(request, val1=0, val2=0):
    return HttpResponse(f"value1 = {val1} and value2 = {val2}")


def viewbook(request, bookId):
    # Mock data: assume these are books in your database
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    targetBook = None

    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook}  # Passing the book data to the template
    return render(request, 'bookmodule/show.html', context)

# Create your views here.