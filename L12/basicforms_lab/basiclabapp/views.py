from email import message
from django.shortcuts import render
from basiclabapp import forms

# Create your views here.

def index(request):
  return render(request, 'basiclabapp/index.html')


def ticket_view(request):
  form = forms.SupportTicketForm()

  if request.method =='POST':
    form = forms.SupportTicketForm(request.POST)
    
    if form.is_valid():
      print("Validation Success!")
      print("Full Name: " + form.cleaned_data['full_name'])
      print("Email: " + form.cleaned_data['email'])
      print("Text: " + form.cleaned_data['text']) 

  return render(request, 'basiclabapp/form_page.html', {'form': form})