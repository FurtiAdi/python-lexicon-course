from django.shortcuts import render
from .models import AccessRecord, WebPage, Topic

# Create your views here.


def index(request):
    context = {
        'insert_title': 'Here are your access records:',
        'insert_column_1_title': 'Site Name',
        'insert_column_2_title': 'Date Accessed',
        'records': AccessRecord.objects.all()
    }
    return render(request, 'index.html', context)
