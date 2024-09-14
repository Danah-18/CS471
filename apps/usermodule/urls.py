from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # Define URL patterns for the usermodule app
    # Add more paths as needed
]
