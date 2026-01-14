from django.conf.urls import url, include
from user_app import views

app_name = 'user_app'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),

]