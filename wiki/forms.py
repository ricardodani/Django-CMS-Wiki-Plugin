# -*- encoding: utf-8 -*-

#from django.forms import ModelForm
from models import WikiPostPlugin
from django import forms

class WikiPostForm(forms.ModelForm):
	
    class Meta:
        model = WikiPostPlugin
