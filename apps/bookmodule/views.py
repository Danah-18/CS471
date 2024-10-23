from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book


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

def links_page(request):
    return render(request, 'bookmodule/links.html')

def text_formatting_page(request):
    return render(request, 'bookmodule/text_formatting.html')

def listing_page(request):
    return render(request, 'bookmodule/listing.html')

def tables_page(request):
    return render(request, 'bookmodule/tables.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':56788765, 'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'A. Burkov'}
    return [book1, book2, book3]

def search_books(request):
    if request.method == "POST":  # Checks if the request is a POST (form submission)
        keyword = request.POST.get('keyword').lower()  # Get the keyword input from the form
        isTitle = request.POST.get('option1')  # Check if the "Title" checkbox was selected
        isAuthor = request.POST.get('option2')  # Check if the "Author" checkbox was selected

        # Retrieve a list of books (from a predefined function or database)
        books = __getBooksList()
        filtered_books = []

        # Iterate over the list of books to check if the keyword matches the title or author
        for book in books:
            contained = False
            if isTitle and keyword in book['title'].lower():  # Match keyword in the title
                contained = True
            if isAuthor and keyword in book['author'].lower():  # Match keyword in the author
                contained = True
            if contained:
                filtered_books.append(book)  # Add matching books to the result

        # Render the results to the 'bookList.html' template, passing the filtered books
        return render(request, 'bookmodule/bookList.html', {'books': filtered_books})

    # If the request is not POST (i.e., when the page is first loaded), render the search form
    return render(request, 'bookmodule/search_form.html')


def insert_multiple_books(request):
    books = [
        Book(title='Continuous Delivery', author='J. Humble and D. Farley', price=120.00, edition=3),
        Book(title='Reversing: Secrets of Reverse Engineering', author='E. Eilam', price=97.00, edition=2),
        Book(title='The Hundred-Page Machine Learning Book', author='Andriy Burkov', price=100.00, edition=4),
    ]
    Book.objects.bulk_create(books)
    return HttpResponse('Multiple books added successfully!')


def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def lookup_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
