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
    path('insert/', views.insert_multiple_books),
    path('insert/', views.insert_multiple_books, name='insert_multiple_books'),
    path('simple/query/', views.simple_query),
    path('simple/query/', views.simple_query, name='simple_query'),
    path('complex/query/', views.lookup_query),
    path('lookup/query/', views.lookup_query, name='lookup_query'),  



]














