# from typing_extensions import Required
from django.contrib import auth, messages
from django.db import models
from django.views.generic.list import ListView
from .models import Contact, User, Job, Organisation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
import os

# Create your views here.

def index(request):
    return render(request, 'index.html')

def jobdescription(request):
    all_Materials = Job.objects.all()
    return render(request, 'jobDescription.html',{"Materials": all_Materials})

def organization(request):
    all_Materials = Organisation.objects.all()
    return render(request, 'organisation.html',{"Materials": all_Materials})

def jobapplication(request):
    return render(request, 'jobApplication.html')

def logoutU(request):
    auth.logout(request)
    return render(request, 'index.html')

# def signup(request):
#     print(request.method)
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         p_reg_form = ProfileRegisterForm(request.POST)
#         if form.is_valid() and p_reg_form.is_valid():
#             user = form.save()
#             user.refresh_from_db()  # load the profile instance created by the signal
#             p_reg_form = ProfileRegisterForm(request.POST, instance=user.profile)
#             p_reg_form.full_clean()
#             p_reg_form.save()
#             messages.success(request, f'Your account has been sent for approval!')
#             return redirect('/')
#         else:
#             form = SignUpForm()
#             return render(request, 'signup.html', {'form': form})
#     else:
#         form = SignUpForm()
#         p_reg_form = ProfileRegisterForm()
#         context = {
#                 'form': form,
#                 'p_reg_form': p_reg_form
# }
#     return render(request, 'signup.html', {'form': form})

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contactus = Contact(name=name, email=email, phone=phone, desc=desc)
        contactus.save()
        # print(name)
    return render(request, 'Contactus.html')

# def login(request):
#     if request.method == "POST":
#         user_name = request.POST.get('user_name')
#         password = request.POST.get('password')
       
        
        # if Users.objects.filter(user_name=user_name, password=password):
        #     user = Users.objects.get(user_name=user_name)
        #     user.save()
        #     print(user)
        #     return redirect('userProfile')
            

        # else:
        #     messages.info(request, "Invalid Credentials")
        #     return redirect('/login.html')

    # return render(request, 'login.html')


# def user_details(request, pk):
#     user = Users.objects.get(pk=pk)
#     if request.method == 'GET':
#         return user

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html',{'form':form})
    
    #     user_name = request.POST.get('user_name')
        
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')
    #     email = request.POST.get('email')
    #     age = request.POST.get('age')
    #     skillset = request.POST.get('skillset')
    #     password = request.POST.get('password')
    #     password_again = request.POST.get('password_again')
    #     if password and password_again and password == password_again and len(str(password)) >= 8:
    #         print(request.POST)
    #         user = User(user_name=user_name, first_name=first_name, last_name=last_name, email=email, age=age, skillset=skillset, password=password, password_again=password_again)
    #         user.save()
    # return render(request, 'register.html')

def catalog(request):
    return render(request, 'catalog.html')

def c1(request):
    return render(request, 'c1.html')

def userProfile(request):
    # user = Users.objects.get(user_name==user_name)
    # return user
    data = User.objects.filter(id=request.user.id) 
    # if "username" == User.username:
    return render(request, 'userProfile.html',{"datas": data})

def jobInfo(request, code):
    # if request == 'POST':
    #     description = request.POST.get('description')
    #     requirements = request.POST.get('requirements')
    #     mail = request.POST.get('mail')
    #     job = Job(description = description, requirements = requirements, mail = mail)
    #     job.save()
    #     return render(request, 'userProfile.html')
    if request == 'GET':
        job = Job.objects.filter(code==code)
        return job
    

class UserDetailView(LoginRequiredMixin,DetailView):
    model=User
    slug_field = "username"
    slug_url_kwarg = "username"

user_detail_view = UserDetailView.as_view()

def organisation_details(request):
    if request.method == 'GET':
        return Organisation.objects.all()
