from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import requests
from .models import Post,Contact

import json

from django.views import generic

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
# from django.contrib.sites.shortcuts import get_current_site
from .forms import SignUpForm
import requests
from django.contrib import messages

# Chnage Password
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm,UserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from.models import About

# This is for Pagination
from django.core.paginator import Paginator

# This is for Social Login
from social_django.models import UserSocialAuth

# class index(generic.ListView):
#     model = About
#     context_object_name = 'my_book_list'   # your own name for the list as a template variable
#     # Get 5 books containing the title war
#     template_name = 'index.html'  # Specify your own template name/location
 



        
def index(request):

    # polls = About.objects.all()  # For  Print all In Home page
    # context_object_name = 'latest_question_list'
    queryset_list = About.objects.all() 

    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joker': joke,
                    'my_book_list' : queryset_list  }
        return render(request, 'index.html', context)
    else:
        firstname = 'Rahul '
        lastname = 'Raj '

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')


        context = {'joker': joke,
                    'my_book_list' : queryset_list }
        return render(request, 'index.html', context)


def contact(request):
    # context_object_name = 'latest_question_list'
    # queryset_list = Contact.objects.all() 
    # queryset_list = 'my_contact_list'

    if request.method == 'POST':
        first_r = request.POST.get( 'fname' )
        last_r = request.POST.get( 'lname' )
        phone_r = request.POST.get( 'phone' )
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(fname = first_r,lname= last_r,phone=phone_r,email=email_r, subject=subject_r, message=message_r)
        c.save()

      

        return render(request, 'thank.html')
    else:
        return render(request, 'contact.html')

# class BlogListView(ListView):

#     model = Post
#     template_name = 'home.html'

def BlogListView(request):
    contact_list = Post.objects.all()
    paginator = Paginator(contact_list, 4) # Show 4 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'home.html', {'contacts': contacts})


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author','description', 'body','image','pub_date']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body','description']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

@login_required
def detail(request):
    return render(request, 'deatil.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        linkedin_login = user.social_auth.get(provider='linkedin')
    except UserSocialAuth.DoesNotExist:
        linkedin_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'settings.html', {
        'github_login': github_login,
        'linkedin_login': linkedin_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })



@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'password.html', {'form': form})


