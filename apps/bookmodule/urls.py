from django.urls import path
from . import views

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
    path('students/city_count', views.city_count_view, name='city_count')
    ]














