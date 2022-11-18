from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django import forms
from .models import Mytodo

class TodoForm(forms.ModelForm):
    task = forms.CharField(max_length = 50, widget=forms.TextInput(attrs = {
        'id': 'todoField', 'placeholder': 'Enter Task'
    }))
    class Meta:
        model = Mytodo
        fields = ['task',]
