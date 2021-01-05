from django import forms
from django.forms import ModelForm

from .models import *

class EmployeeAddForm(ModelForm):
    class Meta:
        model = EmployeeAdd
        fields = '__all__'
