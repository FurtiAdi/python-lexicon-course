from django.urls import path
from .views import add_movie, login_view, home

urlpatterns = [
    path('', login_view),
    path('home/', home),
    path('add/', add_movie), 
]