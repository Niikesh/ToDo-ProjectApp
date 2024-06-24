from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):

    class Meta: #atleast two values should be passed
        model = Task
        fields = '__all__'