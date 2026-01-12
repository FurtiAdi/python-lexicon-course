from django.shortcuts import render
from App.models import Topic, WebPage, AccessRecord

# Create your views here.
def index(request):
  Webpages_list = AccessRecord.objects.order_by('date')
  date_dict = {'access_records': Webpages_list}
  my_dict = {
        'insert_me': "Hello I am from views.py!"
    }
  return render(request, 'index.html', context=my_dict)