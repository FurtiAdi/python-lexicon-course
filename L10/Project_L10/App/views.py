from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {
        'insert_welcome_message' : "Welcome to the Python Lexicon Course!",
        'insert_course_name' : "Course Name: Python & AI",
        'insert_student_today' : "Students Today: 33",
        'insert_me' : "Student Name: Fortuna"
    }
    return render(request, 'index.html', context=my_dict)