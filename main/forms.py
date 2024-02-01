# import form class from django
from typing import Any
from django import forms
 
# import GeeksModel from models.py
from .models import Record, Category, Expenses
 
# create a ModelForm
class RecordForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Record
        fields = ["name"]
        
    def save(self, commit=True, *args, **kwargs):
        user = kwargs.pop('user', None)
        instance = super().save(commit=False, *args, **kwargs)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance
        

class CategoryForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Category
        fields = "__all__"
        

class ExpensesForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Expenses
        fields = "__all__"
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }