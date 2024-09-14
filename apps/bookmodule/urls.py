from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # Maps the root URL of the bookmodule to the index view
    path('index2/<int:val1>/<int:val2>/', views.index2),  # Maps a URL with two integer parameters to the index2 view
    path('<int:bookId>/', views.viewbook),  # Adding a new path for book details
]
