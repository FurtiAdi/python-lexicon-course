from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "bookstore_app/home.html")

def about(request):
    return render(request, "bookstore_app/about.html")

def book(request):
    return render(request, "bookstore_app/book.html")