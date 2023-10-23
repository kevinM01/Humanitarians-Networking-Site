from django.contrib import admin
from django.urls import path
from Home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name = 'index'),
    path('contactus', views.contactus,name = 'contactus'),
    # path('signup.html', views.signup,name = 'signup.html'),
    path('register', views.register,name = 'register'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'),name = 'login'),
    path('c1.html', views.c1,name = 'c1.html'),
    path('catalog.html', views.catalog,name = 'catalog.html'),
    path('userProfile', views.userProfile,name = "userProfile"),
    path("<str:username>/", view = views.user_detail_view,name="detail"),
    path('jobdescription', views.jobdescription,name = 'jobdescription'),
    path('jobapplication', views.jobapplication,name = 'jobapplication'),
    path('organization', views.organization,name = 'organization'),
    path('logout', views.logoutU,name = 'logout'),


]