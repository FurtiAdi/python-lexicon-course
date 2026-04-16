from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .azure_utils import upload_file_to_azure

def upload_view(request):
    file_url = None

    if request.method == "POST":
        file = request.FILES.get("file")

        if file:
            file_url = upload_file_to_azure(file)

    return render(request, "upload.html", {"file_url": file_url})