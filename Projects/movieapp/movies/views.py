from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from azure.cosmos import CosmosClient
from .services import CosmosService

service = CosmosService()

# LOGIN VIEW
def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )
        if user:
            login(request, user)
            return redirect("/home/")
        else:
            return render(request, "login.html", {"error": "Invalid login"})
    return render(request, "login.html")

# HOME VIEW 
@login_required
def home(request):
    query = request.GET.get("q")

    try:
        items = service.get_items()
    except:
        items = []
    
    if query:
        items = [
            m for m in items
            if query.lower() in m.get("title", "").lower()
        ]

    return render(request, "home.html", {
        "movies": items,
        "error": "Could not load movies" if not items else None
    })

@login_required
def add_movie(request):
    if request.method == "POST":
        data = {
            "id": request.POST.get("id"),
            "title": request.POST.get("title"),
            "genre": request.POST.get("genre").split(","),
            "year": int(request.POST.get("year")),
            "ratings": [],
            "details": {
                "director": request.POST.get("director"),
                "duration": int(request.POST.get("duration"))
            }
        }
        service.create_item(data)
        return redirect("/home/")
    return render(request, "add_movie.html")