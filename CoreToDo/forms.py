from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class TaskForm(forms.ModelForm):

    class Meta: #atleast two values should be passed
        model = Task
        fields = '__all__'

class CreateUserForm(UserCreationForm):
 
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]