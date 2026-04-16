from django.conf.urls import url, include
from blog_app import views

app_name = 'blog_app'

urlpatterns = [
    url(r'^blog/', views.blog, name='blog'),
    url(r'^user_login/', views.user_login, name='user_login'),
    url(r'^user_profile/', views.user_profile, name = 'user_profile'),
    url(r'^register/', views.register, name='register')

]