from django import forms
from django.db import models
from django.contrib.auth.models import User
from .models import TechNews
from django.http import request
from datetime import date

class TechNewsForm(forms.ModelForm):
    
    class Meta:
        model = TechNews
        
        fields = ["heading", "part_1", "part_2", 'author', "timeline"]

    def __init__(self, *args, **kwargs):
        super(TechNewsForm, self).__init__(*args, **kwargs)
        # Hide the user and date_field using widgets
        self.fields['author'].widget = forms.HiddenInput()
        self.fields['timeline'].widget = forms.HiddenInput()
    
  