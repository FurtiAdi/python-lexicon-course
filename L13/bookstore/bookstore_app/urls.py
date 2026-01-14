from django.conf.urls import url, include
from bookstore_app import views

#TEMPLATE TAGGING
app_name = 'bookstore_app'

urlpatterns = [
  url(r'^about/$', views.about, name='about'),    
  url(r'^book/$', views.book, name='book'),
]