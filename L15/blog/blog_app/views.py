from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from blog_app.forms import UserForm, UserProfileInfoForm

# Create your views here.

def index(request):
    return render(request, 'blog_app/index.html')

def blog(request):
    return render(request, 'blog_app/blog.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user  = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()
        
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'blog_app/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username  = request.POST.get('username')
        password  = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'blog_app/login.html', {})
    
@login_required
def user_profile(request):
    if request.user.is_authenticated:
        user = request.user
        profile = user.userprofileinfo
        context = {
            'username': profile.get_full_name(),
            'email': profile.get_email(),
            'linkedin_site': profile.get_portfolio_site(),
            'profile_pic': profile.get_profile_pic()
        }
        return render(request, 'blog_app/profile.html', context)
        
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))