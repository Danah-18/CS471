from django.shortcuts import render, get_object_or_404

# Sample data for demonstration purposes
BOOKS = [
    {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'},
    {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'},
    {'id': 1, 'title': 'Internet & World Wide Web How To Program', 'author': 'Deitel, Deitel'}

]

def index(request):
    name = request.GET.get("name", "world!")
    return render(request, "bookmodule/index.html", {"name": name})

def list_books(request):
    # Pass sample data to the list_books template
    return render(request, 'bookmodule/list_books.html', {'books': BOOKS})

def viewbook(request, bookId):
    # Find the book by ID or return a 404 error if not found
    targetBook = next((book for book in BOOKS if book['id'] == bookId), None)
    
    # If the book is not found, use get_object_or_404 for a proper 404 response
    if targetBook:
        context = {'book': targetBook}
        return render(request, 'bookmodule/show.html', context)  # Use the show.html for details
    else:
        return render(request, 'bookmodule/one_book.html', {'book': None})  # Handle not found scenario

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')
