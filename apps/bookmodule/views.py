from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from .models import Address, Book, Student,Student2, Address2, ProfilePicture
from django.db.models import Count, Sum, Avg, Max, Min
from .forms import BookForm, StudentForm, AddressForm , Student2Form, Address2Form, ProfilePictureForm



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

#lab7
def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def lookup_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')

#lab 8
def task1_view(request):
    books = Book.objects.filter(Q(price__lte=50))
    return render(request, 'bookmodule/task1.html', {'books': books})

def task2_view(request):
    books = Book.objects.filter(Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/task2.html', {'books': books})

def task3_view(request):
    books = Book.objects.filter(~Q(edition__gt=2) & ~(Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/task3.html', {'books': books})

def task4_view(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': books})

def task5_view(request):
    aggregates = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'aggregates': aggregates})

def city_count_view(request):
    city_counts = Student.objects.values('address__city').annotate(student_count=Count('id'))
    return render(request, 'bookmodule/city_count.html', {'city_counts': city_counts})

def task7_view(request):
    data = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task7.html', {'data': data})


#lab 9 pt1
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part1/listbooks.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        edition = request.POST['edition']
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return redirect('list_books')
    return render(request, 'bookmodule/lab9_part1/addbook.html')

def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == "POST":
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.edition = request.POST['edition']
        book.save()
        return redirect('list_books')
    return render(request, 'bookmodule/lab9_part1/editbook.html', {'book': book})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('list_books')

#lab9 pt2
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part2/listbooks.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab9_part2/addbook.html', {'form': form})

def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab9_part2/editbook.html', {'form': form})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('list_books')


#lab 10
# List all students
def list_students(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/list_students.html', {'students': students})

# Add a student
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_students')  
    else:
        form = StudentForm()
    return render(request, 'bookmodule/add_student.html', {'form': form})

# Update a student
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'bookmodule/update_student.html', {'form': form})

# Delete a student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('list_students')

#lab10 Task2
def list_students2(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/list_students2.html', {'students': students})        

def add_student2(request):
    if request.method == 'POST':
        form = Student2Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form()
    return render(request, 'bookmodule/add_student2.html', {'form': form})

def update_student2(request, id):
    student = get_object_or_404(Student2, id=id)
    if request.method == 'POST':
        form = Student2Form(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form(instance=student)
    return render(request, 'bookmodule/update_student2.html', {'form': form})

def delete_student2(request, id):
    student = get_object_or_404(Student2, id=id)
    student.delete()
    return redirect('list_students2')

#lab10 Task3
def upload_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = ProfilePictureForm()
    return render(request, 'bookmodule/upload_picture.html', {'form': form})

