from django import forms
from .models import car
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class carform(forms.ModelForm):
    class Meta:
        model = car
        fields = ['carmodel','photo', 'description']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
