from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

CHOICES= [
    ('Fellow', 'Fellow'),
    ('Mentor', 'Mentor'),
    ('Volunteer', 'Volunteer'),
    ('Employee', 'Employee'),
    ('Mentee', 'Mentee')
    ]

class UserRegisterForm(UserCreationForm):
    role= forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    class Meta():
        model = User
        fields = ['username','first_name','last_name','email','age','role','skillset','password1','password2']