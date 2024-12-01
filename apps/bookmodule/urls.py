from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="books.index"), 
    path('list_books/', views.list_books, name="books.list_books"), 
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"), 
    path('aboutus/', views.aboutus, name="books.aboutus"), 
    path('html5/links/', views.links_page, name='links_page'),
    path('html5/text/formatting/', views.text_formatting_page, name='text_formatting_page'),
    path('html5/listing/', views.listing_page, name='listing_page'),
    path('html5/tables/', views.tables_page, name='tables_page'),
    path('search/', views.search_books, name='search_books'),
    path('insert/', views.insert_multiple_books, name='insert_multiple_books'),
    path('simple/query/', views.simple_query, name='simple_query'),
    path('complex/query/', views.lookup_query),
    path('lookup/query/', views.lookup_query, name='lookup_query'), 
     
    #lab 8
    path('task1/', views.task1_view, name='task1'),
    path('task2/', views.task2_view, name='task2'),
    path('task3/', views.task3_view, name='task3'),
    path('task4/', views.task4_view, name='task4'),
    path('task5/', views.task5_view, name='task5'),
    path('task7/', views.task7_view, name='task7'),
    path('students/city_count', views.city_count_view, name='city_count'),
    
    #lab 9 pt1
    path('books/lab9_part1/listbooks', views.list_books, name='list_books'),
    path('books/lab9_part1/addbook',views.add_book, name= 'add_book'),
    path('books/lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
    path('books/lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),
    #lab9 pt2
    path('books/lab9_part2/listbooks', views.list_books, name='list_books'),
    path('books/lab9_part2/addbook', views.add_book, name='add_book'),
    path('books/lab9_part2/editbook/<int:id>', views.edit_book, name='edit_book'),
    path('books/lab9_part2/deletebook/<int:id>', views.delete_book, name='delete_book'),
    
    #lab10 Task1
    path('add_student/', views.add_student, name='add_student'),
    path('students/', views.list_students, name='list_students'),
    path('update_student/<int:id>/', views.update_student, name='update_student'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
    #lab10 Task2
    path('add_student2/', views.add_student2, name='add_student2'),
    path('students2/', views.list_students2, name='list_students2'),  
    path('update_student2/<int:id>/', views.update_student2, name='update_student2'),  
    path('delete_student2/<int:id>/', views.delete_student2, name='delete_student2'), 
    #lab10 Task3
    path('images/', views.upload_profile_picture, name='upload_profile_picture'),
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)